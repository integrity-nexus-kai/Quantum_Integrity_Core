#!/usr/bin/env python3
"""Create and verify a standalone source ZIP; never submit or publish it."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import zipfile


INPUTS = {
    'main.tex': 'submission/arxiv/main.tex',
    'references.bib': 'submission/arxiv/references.bib',
    'unsrtnat.bst': 'submission/arxiv/unsrtnat.bst',
    'figures/tig_horizon_branches.png': 'figures/tig_horizon_branches.png',
    'LICENSE': 'LICENSE',
}


def export(root, output):
    output.mkdir(parents=True,exist_ok=True)
    zip_path=output/'arxiv_source.zip'
    members=[]
    with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,path in sorted(INPUTS.items()):
            data=(root/path).read_bytes()
            info=zipfile.ZipInfo(name,date_time=(2026,10,2,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            z.writestr(info,data)
            members.append({'name':name,'source':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
    # Verify only extracted ZIP members can satisfy non-system build inputs.
    with tempfile.TemporaryDirectory(prefix='qic-arxiv-isolated-') as tmp:
        work=Path(tmp)
        with zipfile.ZipFile(zip_path) as z:
            assert sorted(z.namelist())==sorted(INPUTS)
            assert z.testzip() is None
            z.extractall(work)
        for entry in members:
            assert hashlib.sha256((work/entry['name']).read_bytes()).hexdigest()==entry['sha256']
        log=output/'export_build.stdout.log'
        with log.open('w') as stream:
            result=subprocess.run(['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=work,stdout=stream,stderr=subprocess.STDOUT)
            if result.returncode:raise RuntimeError('Standalone latexmk build failed')
            for _ in range(2):
                result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','main.tex'],cwd=work,stdout=stream,stderr=subprocess.STDOUT)
                if result.returncode:raise RuntimeError('Standalone final PDF pass failed')
        final_log=(work/'main.log').read_text(errors='replace')
        for marker in ['Warning','Overfull','undefined']:
            if marker in final_log:raise RuntimeError('Standalone final log: '+marker)
        for filename in ['main.pdf','main.log','main.bbl','main.fls']:
            shutil.copyfile(work/filename,output/('arxiv.pdf' if filename=='main.pdf' else 'export_'+filename))
        # Confirm every local .fls input belongs to the extracted ZIP or generated files.
        observed=[line[6:] for line in (work/'main.fls').read_text().splitlines() if line.startswith('INPUT ')]
        local=[name.replace(str(work)+'/', '') for name in observed if str(work) in name or not name.startswith('/')]
        for name in observed:
            if name.startswith('/') and not (name.startswith(str(work)+'/') or name.startswith(('/usr/','/var/lib/texmf/','/etc/texmf/'))):
                raise RuntimeError('Unbound absolute export input: '+name)
        if any('../../figures' in name for name in observed):
            raise RuntimeError('Export still depends on parent repository figure')
    manifest={'object_class':'EXPORTED_PACKAGE_OBJECT','release':'NONE','submitted':False,
              'source_members':members,'zip_sha256':hashlib.sha256(zip_path.read_bytes()).hexdigest(),
              'zip_bytes':zip_path.stat().st_size,'isolated_build':'PASS','final_latex_warnings':0,
              'local_input_paths':sorted(set(local)),
              'arxiv_pdf_sha256':hashlib.sha256((output/'arxiv.pdf').read_bytes()).hexdigest()}
    (output/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return manifest


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    print(json.dumps(export(Path(__file__).resolve().parents[1],args.output_dir.resolve()),indent=2))


if __name__=='__main__':
    main()
