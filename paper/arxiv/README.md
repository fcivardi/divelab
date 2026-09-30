# arXiv source package

main.tex embeds the bibliography and refers only to seven PNGs under
generated/. It compiles with standard pdfLaTeX packages without Quarto.

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

From paper/, refresh the source using bash tools/build_paper.sh.
Upload a ZIP or tar.gz containing main.tex and generated/*.png, retaining
relative paths. Exclude logs, auxiliary files and the compiled PDF from the
TeX submission; the PDF is for author preview.

Author metadata, category, distribution license and submission are chosen
by the author. Local compilation does not establish arXiv acceptance.
