# Computational validation record

Validation date: 2026-08-09

Branch source: `editorial-v2`

Environment: Python 3.12, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8

## Result

All 18 canonical notebooks executed successfully in order, with zero Python
exceptions. The run produced 66 Matplotlib figures.

| Notebooks | Passed | Failed | Figures |
|---:|---:|---:|---:|
| 18 | 18 | 0 | 66 |

## Representative numerical checks

| Experiment | Result |
|---|---:|
| Pressure gradient | 10051.82 Pa/m |
| Linearized open-loop poles | +0.102663, -0.102663 1/s |
| Unstable-mode e-folding time | 9.741 s |
| Observer velocity RMSE | 0.00078 m/s |
| Finite-difference velocity RMSE | 1.4356 m/s |
| Designed closed-loop poles | -0.6, -0.9 1/s |
| PID final error in test case | approximately 0 m |
| Anti-windup IAE | 5.17 m·s |
| Windup IAE | 177.47 m·s |
| Kalman velocity RMSE | 0.01593 m/s |

These values are regression anchors for the paper, not empirical measurements
of real divers. Before submission, CI will repeat execution through a real
Jupyter kernel and compare selected values against explicit tolerances.
