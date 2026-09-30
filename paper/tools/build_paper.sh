#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p arxiv/generated
cp generated/*.png arxiv/generated/
pandoc index.qmd --from markdown --to latex --standalone --citeproc \
  --bibliography=references.bib --resource-path=. --number-sections \
  -V geometry:margin=1in -V colorlinks:true -o arxiv/main.tex
cd arxiv
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
