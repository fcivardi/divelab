# DiveLab arXiv paper

The paper presents an executable control-engineering curriculum. The physical
instability mechanism is established modeling material; the contribution is
the coherent curriculum, traceable notebook sequence and verified artifact.
No measured learning gains are claimed.

## Reproduce the release validation

Use Python 3.12 from the repository root:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r paper/requirements-lock.txt
.venv/bin/python paper/tools/validate_kernel.py
.venv/bin/python paper/tools/check_model.py
```

The kernel validator executes 18 notebooks in separate Jupyter kernels,
exports 64 figures, checks 19 numerical anchors, and verifies that the seven
manuscript figure selections exist. Reports are written under paper/_build/.
The model checker tests 54 physical-parameter combinations and nine observer
sample-period/random-seed combinations. Jupyter requires local sockets.
The committed validation-results.json and model-check-results.json record
the 2026-09-30 run. VALIDATION.md describes the evidence and its limits.
The older tools/validate_notebooks.py is an execution fallback, not the
canonical release test.

## Build the manuscript

With Pandoc and pdfLaTeX installed:

```bash
bash paper/tools/build_paper.sh
```

This refreshes paper/arxiv/main.tex, copies the selected figures, and compiles
twice. The PDF is paper/arxiv/main.pdf (ignored by Git). The raw LaTeX
curriculum table intentionally keeps the PDF table together.

.github/workflows/paper.yml repeats the kernel, model and independent LaTeX
checks on the paper branch and relevant PRs.

## Submission package

Upload main.tex and the seven files under arxiv/generated/, preserving their
relative paths. Bibliography entries are embedded in main.tex by Pandoc.
See arxiv/README.md and FINAL_REVIEW.md.

The models are educational, not operational dive planning or equipment
validation. Author metadata, arXiv category and submission remain author
decisions.
