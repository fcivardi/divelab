# arXiv source package

`main.tex` is the standalone LaTeX source generated from `paper/index.qmd` with
Pandoc and citeproc. The `generated/` directory contains the seven figures
selected from the executable notebooks.

To refresh and test this directory from `paper/`:

```bash
mkdir -p arxiv/generated
cp generated/*.png arxiv/generated/
pandoc index.qmd --from markdown --to latex --standalone --citeproc \
  --bibliography=references.bib --resource-path=. --number-sections \
  -V geometry:margin=1in -V colorlinks:true -o arxiv/main.tex
(cd arxiv && pdflatex -interaction=nonstopmode -halt-on-error main.tex)
```

The generated `main.pdf` and LaTeX auxiliary files are intentionally ignored.
Before submission, create a versioned repository release and replace the
provisional code-availability statement with its archival identifier.
