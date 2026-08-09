# DiveLab arXiv paper

This directory contains the standalone research paper derived from the DiveLab
book and its 18 executable notebooks. The book remains the full educational
resource; the paper states and evaluates the narrower methodological and
computational contribution.

## Working title

**DiveLab: An Executable Framework for Teaching Control Engineering Through
Scuba-Diving Dynamics**

## Reproduce the computational evidence

From the repository root:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r paper/requirements.txt
MPLBACKEND=Agg MPLCONFIGDIR=/tmp/divelab-mpl \
  .venv/bin/python paper/tools/validate_notebooks.py
```

The validator executes every code cell in notebook order, reports numerical
failures, exports all Matplotlib figures to `/tmp/divelab-executed`, and refreshes
the seven selected manuscript figures in `paper/generated/`. A
Jupyter-kernel CI job will provide the independent canonical validation before
submission.

## Build the manuscript

With Quarto installed, run:

```bash
quarto render paper/index.qmd --to pdf --output-dir _build
```

For a minimal local build using Pandoc and pdfLaTeX:

```bash
mkdir -p paper/_build
pandoc paper/index.qmd --from markdown --to pdf --pdf-engine=pdflatex \
  --citeproc --bibliography=paper/references.bib --resource-path=paper \
  --number-sections -V geometry:margin=1in -V colorlinks:true \
  -o paper/_build/divelab-arxiv-draft.pdf
```

## Submission boundary

The manuscript describes an educational modeling framework. It does not claim
measured learning gains, provide operational dive tables, certify equipment, or
replace diver training, medical assessment, or validated dive-planning tools.
