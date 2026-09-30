# Computational validation record

Validation date: 2026-09-30.

Canonical notebook source: commit 7f7a3db64f7bb7fcf0570e4496a9900de7f5172e.
The release review changes paper tooling and text, not notebook source.

## Kernel execution

All 18 canonical notebooks passed in separate Jupyter kernels. Original code
cells execute in document order; an injected capture step exports and closes
figures after each cell using Agg. An audit cell checks numerical anchors.
This tests kernel execution, not the Colab UI.

| Notebooks | Passed | Failed | Figures | Numerical anchors |
|---:|---:|---:|---:|---:|
| 18 | 18 | 0 | 64 | 19 |

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8,
nbformat 5.11.1, nbclient 0.11.0 and ipykernel 7.4.0. The dependency closure
is pinned in requirements-lock.txt.

validation-results.json contains actual values, expected values and absolute
tolerances; relative tolerance is zero. The poles are approximately
+/-0.10266257 s^-1 and the e-folding time is 9.74064828 s.
Observer and differentiation RMSE are evaluated over 5--20 s, excluding the
initial transient. Windup/anti-windup IAE are 177.46660855/5.17334574 m s.

## Independent model and sensitivity checks

54 cases combine mass (65, 85, 105 kg), water density (1000, 1025 kg/m^3),
depth (5, 20, 35 m) and surface-equivalent gas volume (4, 8, 12 L).
All satisfy neutral force balance, agree with the finite-difference buoyancy
derivative, exhibit opposite-sign real poles, and admit prescribed local
closed-loop poles when gains are redesigned. This is a model-consistency
sweep, not a fixed-controller robustness test.

Nine observer scenarios combine sample periods 0.005, 0.01, 0.02 s with
random seeds 7, 42, 101 at depth-noise SD 0.02 m. Post-transient observer
RMSE ranges from 0.000514 to 0.001280 m/s; differentiation ranges from
0.6763 to 2.8432 m/s. This limited sensitivity check supports the example,
not a claim about hardware. Full results: model-check-results.json.

## Evidence boundary

Gas-law derivative, force and acceleration relations have consistent SI
dimensions. Fresh kernels eliminate cross-notebook state. Regression checks
cannot establish physical fidelity or learning gains. Added hydrodynamic
mass and valve dynamics are outside the minimal plant. Capstone resource
histories use prescribed depth; local feedback is a separate experiment.

The historical 2026-08-09 record reported 66 figures. The current revision
exports 64; manuscript and release record now report the reproduced count.
