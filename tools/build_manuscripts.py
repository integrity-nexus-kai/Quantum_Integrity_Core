#!/usr/bin/env python3
"""Build the two independent QIC manuscript packages; no release action."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", choices=("paper", "arxiv", "all"), nargs="?", default="all")
    parser.add_argument("--output-dir", type=Path, help="Build directory; default: repository .build")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    output = (args.output_dir or root / ".build").resolve()
    if not shutil.which("latexmk") or not shutil.which("pdflatex"):
        parser.error("latexmk and pdflatex must be installed")
    packages = {"paper": root / "papers/tig-paper", "arxiv": root / "submission/arxiv"}
    selected = packages if args.package == "all" else {args.package: packages[args.package]}
    results = []
    for name, source in selected.items():
        dest = output / name
        dest.mkdir(parents=True, exist_ok=True)
        command = ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "-outdir=" + str(dest), "main.tex"]
        with (dest / "latexmk.stdout.log").open("w") as log:
            result = subprocess.run(command, cwd=source, stdout=log, stderr=subprocess.STDOUT, check=False)
        results.append({"package": name, "returncode": result.returncode, "pdf": str(dest / "main.pdf"), "log": str(dest / "latexmk.stdout.log")})
    print(json.dumps(results, indent=2))
    return 0 if all(item["returncode"] == 0 for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
