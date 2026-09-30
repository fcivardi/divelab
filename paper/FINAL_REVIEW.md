# Final pre-submission review

Date: 2026-09-30. Reviewer: automated technical and editorial review assisted
by OpenAI ChatGPT; final responsibility remains with Francesco Civardi.

## Outcome

The paper passes the local computational and source-package checks. The
manuscript is prepared for author review and arXiv submission. This does not
establish experimental validity, measured learning gains, or arXiv acceptance.

## Checks completed

- All 18 notebooks executed in separate Jupyter kernels in both the existing
  scientific environment and a fresh virtual environment installed solely
  from requirements-lock.txt: 64 figures and 19 numerical anchors passed.
- 54 model parameter combinations passed neutral-balance, finite-difference
  derivative, local saddle and redesigned closed-loop pole checks.
- Nine observer scenarios varied sample period and random seed. The reported
  nominal RMSE values reproduced, with a better observer RMSE than direct
  differentiation in each specified scenario.
- Seven DOI-bearing references were verified against Crossref metadata.
  Author/year/volume/page information agrees with the cited editions; the
  Mathematics article appeared online in December 2022 in its 2023 volume.
  The bibliography also contains two standard textbooks and the new
  arXiv:2608.14978 preprint. Ten references are cited and resolved.
- SI dimensions, mixed coordinate signs, buoyancy derivative, linearization,
  observability and feedback signs were reviewed. Quadratic drag has zero
  derivative at rest and is correctly omitted from the infinitesimal plant.
- The standalone LaTeX package compiles twice to an 11-page PDF. All seven
  figures are included by relative path. There are no unresolved citations,
  undefined references, missing figures or overfull boxes. All pages were
  rendered and visually inspected. Minor underfull table cells are harmless.

## Corrections made

- Corrected the historical figure count from 66 to 64.
- Added a complete dependency lock, a kernel validator with numerical
  tolerances, model/sensitivity checks and a dedicated GitHub Actions workflow.
- Specified gas volume, surface pressure, observer noise/sample rate, initial
  states, RMSE evaluation window and anti-windup experiment settings.
- Clarified that the resource-history capstone uses prescribed depth and that
  local feedback is a separate experiment. Its -0.306 m final offset is the
  expected PD response to a 5 N disturbance, not dive-profile tracking error.
- Updated related work and explicitly excluded priority claims for the
  compressible-buoyancy saddle or delayed diver feedback.
- Regenerated the seven figures, updated source/validation documentation,
  kept the curriculum table together and improved float placement.

## Submission decisions

The author must choose the final arXiv category and distribution license,
review the author metadata and AI-use acknowledgement, and perform submission.
The public PR carries the automated CI status. No submission has been made
as part of this review, and the paper branch has not been merged.
