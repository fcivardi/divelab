# DiveLab v1.1 R2 — Formatting correction notes

This package contains corrected canonical Notebooks **14–21 only**.

## Correction method

The notebooks were rebuilt directly from the canonical GitHub ZIP supplied for v1.0.

Only Markdown math delimiters were changed:

- `\[ ... \]` → `$$ ... $$`
- `\( ... \)` → `$ ... $`

No Markdown parser, Pandoc conversion, or equation rewriting was used. The mathematical content is therefore preserved exactly, including equals signs, fractions, integrals, braces, subscripts, and Greek symbols.

## Structural validation

For every notebook 14–21:

- no `\[` / `\]` delimiters remain;
- no `\(` / `\)` delimiters remain;
- no malformed LaTeX equations enclosed in ordinary `[ ... ]` brackets remain;
- every Markdown cell has balanced `$$` display delimiters;
- the Colab badge points to the matching canonical GitHub path.

## Notebook 14 spot-check

The corrected source contains:

```markdown
$$
\dot x(t)+a x(t)=u(t).
$$
```

and:

```markdown
$$
F(s)
=
\mathcal{L}\{f(t)\}
=
\int_0^\infty f(t)e^{-st}\,dt.
$$
```

and inline math such as:

```markdown
$\sigma$
```

rather than `(\sigma)`.

## Files

- 14_Laplace_Transforms.ipynb
- 15_Transfer_Functions.ipynb
- 16_PID_Control.ipynb
- 17_Frequency_Response.ipynb
- 18_Breathing_Dynamics.ipynb
- 19_Gas_Consumption.ipynb
- 20_Dive_Computers.ipynb
- 21_Decompression_Models.ipynb

Replace only these eight files in the repository.
