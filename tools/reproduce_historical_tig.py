#!/usr/bin/env python3
"""Forensic reconstruction of the May 3 PDF; compiler failures stay explicit.

An exit code of zero means the reconstructed PDF content matches the archive.
It does NOT mean pdflatex/BibTeX completed without errors or that a paper is ready.
Dependencies: pdflatex, BibTeX, PyMuPDF (fitz). No input manuscript is edited.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "papers/archive/source_bindings/tig_2026-05-03/main.tex"
PDF = ROOT / "papers/tig-paper/TIG_Paper.pdf"
SOURCE_SHA256 = "9d6d183b159cec956058efbff0bb270760cab94af738c537a76ede6283e742b5"
PDF_SHA256 = "40eb555066bd1609a7d6e32154a88c56356773aef704d08b72076f8e2d0a8a87"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source_data = SOURCE.read_bytes()
    if hashlib.sha256(source_data).hexdigest() != SOURCE_SHA256:
        raise ValueError("Historical source fingerprint changed")
    if hashlib.sha256(PDF.read_bytes()).hexdigest() != PDF_SHA256:
        raise ValueError("Archived PDF fingerprint changed")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    # Isolate the missing-file reconstruction from all current repo inputs.
    with tempfile.TemporaryDirectory(prefix="qic-may3-") as folder:
        work = Path(folder)
        (work / "main.tex").write_bytes(source_data)
        (work / "build").mkdir()
        (work / "font_tmp").mkdir()
        env = dict(os.environ, TMPDIR=str(work / "font_tmp"))
        tex = ["pdflatex", "-interaction=nonstopmode", "-no-shell-escape",
               "-recorder", "-output-directory=build", "main.tex"]
        commands = [(tex, work), (["bibtex", "main.aux"], work / "build"),
                    (tex, work), (tex, work)]
        runs = []
        for i, (command, cwd) in enumerate(commands, 1):
            run = subprocess.run(command, cwd=cwd, env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            (work / "build" / f"pass_{i}.log").write_bytes(run.stdout)
            runs.append({"command": command, "cwd": "build" if cwd.name == "build" else ".",
                         "exit_code": run.returncode, "console_log": f"pass_{i}.log"})
        output = work / "build/main.pdf"
        if not output.exists():
            raise RuntimeError(f"No forensic PDF produced: {runs}")
        historic = fitz.open(PDF)
        rebuilt = fitz.open(output)
        rows = [{"page": i + 1,
                 "text_equal_after_bullet_encoding_normalization":
                 historic[i].get_text().replace("\x88", "•") ==
                 rebuilt[i].get_text().replace("\x88", "•")}
                for i in range(min(len(historic), len(rebuilt)))]
        matched = len(historic) == len(rebuilt) == 4 and all(
            row["text_equal_after_bullet_encoding_normalization"] for row in rows)
        result = {"purpose": "FORENSIC_CONTENT_COMPARISON_ONLY", "runs": runs,
                  "clean_compilation": all(run["exit_code"] == 0 for run in runs),
                  "historical_source_sha256": SOURCE_SHA256,
                  "historical_pdf_sha256": PDF_SHA256,
                  "reconstructed_pdf_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
                  "page_comparison": rows, "source_content_binding_verified": matched,
                  "exact_original_compiler_or_input_state_proven": False}
        (work / "build/result.json").write_text(json.dumps(result, indent=2) + "\n")
        destination = args.output_dir.resolve() / "forensic_build"
        if destination.exists():
            raise FileExistsError(f"Choose a fresh output directory: {destination}")
        shutil.copytree(work / "build", destination)
        print(json.dumps(result, indent=2))
        historic.close()
        rebuilt.close()
        return 0 if matched else 1


if __name__ == "__main__":
    raise SystemExit(main())
