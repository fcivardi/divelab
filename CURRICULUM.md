# DiveLab Curriculum

> **Understand → Model → Estimate → Control → Integrate**

DiveLab is an executable engineering textbook that uses scuba diving as one coherent case study for physics, dynamical systems, estimation, simulation, and control.

This document defines the **editorial-v2 curriculum**. Version 1.0 is frozen; the chapters and canonical notebooks listed here are the current development path toward Version 2.

It complements:

- `README.md` — the project overview and entry point;
- `ROADMAP.md` — editorial direction and release planning;
- `ARCHITECTURE.md` — repository and component organization;
- `STYLE_GUIDE.md` — manuscript and notebook conventions.

---

## 1. Curriculum purpose

DiveLab develops a single causal model progressively:

$$
\text{depth}
\rightarrow \text{pressure}
\rightarrow \text{gas volume}
\rightarrow \text{buoyant force}
\rightarrow \text{vertical motion}
\rightarrow \text{state}
\rightarrow \text{estimation}
\rightarrow \text{feedback control}.
$$

The final part reconnects this control-engineering spine to breathing, gas-resource, sensing, and inert-gas models. The objective is not to reproduce a dive planner or teach diving technique. It is to teach how engineers move from physical reasoning to models, executable experiments, uncertainty, and controlled dynamic behavior.

At the end of the curriculum, a learner should be able to:

1. derive and interpret the principal physical relationships used in the book;
2. translate a physical description into static and dynamic mathematical models;
3. distinguish states, inputs, disturbances, parameters, measurements, estimates, and predictions;
4. simulate nonlinear and linearized systems in Python;
5. analyze equilibria, stability, observability, and frequency response;
6. implement deterministic and stochastic state estimators;
7. design and assess elementary feedback and PID controllers;
8. explain the effects of delay, noise, saturation, uncertainty, and human intervention;
9. connect subsystem models into an integrated educational simulation;
10. state clearly where a teaching model ceases to support real-world conclusions.

---

## 2. Intended audience and entry requirements

DiveLab is intended for undergraduate engineering students, technically experienced divers, instructors, and independent learners interested in control engineering through a concrete physical system.

The book is progressive, but it is **not a mathematics or Python primer**. A reader beginning the complete curriculum should already be comfortable with:

- high-school physics, algebra, functions, graphs, and SI units;
- elementary differential and integral calculus;
- vectors, matrices, and systems of linear equations;
- first- and second-order ordinary differential equations;
- basic probability concepts;
- basic Python syntax and running cells in a Jupyter or Google Colab notebook.

Later chapters introduce additional ideas when they become necessary, including eigenvalues, covariance matrices, complex numbers, Laplace transforms, and numerical simulation. Readers unfamiliar with these topics can still follow the physical narrative, but should expect to consult a supporting mathematics or Python resource.

No prior course in control theory, state estimation, or diving science is assumed. Practical diving knowledge is helpful context, not an academic prerequisite.

---

## 3. Learning method

Each chapter and notebook pair follows the preferred DiveLab rhythm:

$$
\text{engineering question}
\rightarrow \text{physical intuition}
\rightarrow \text{model}
\rightarrow \text{simulation}
\rightarrow \text{interpretation}
\rightarrow \text{exercise}.
$$

The book provides the connected argument. The notebook is the executable laboratory. Learners should read the chapter first, run the companion notebook in order, change at least one parameter, and explain the result in physical and systems terms.

---

## 4. Curriculum structure

The editorial-v2 curriculum contains **18 chapters and 18 canonical companion notebooks** in four parts.

| Part | Theme | Curriculum question | Chapters |
|:--|:--|:--|:--:|
| I | Physics of Diving | How does depth produce vertical motion? | 1–4 |
| II | Dynamical Systems | How do we represent, analyze, and estimate the system state? | 5–8 |
| III | Control Engineering | How does feedback shape dynamic behavior? | 9–13 |
| IV | Integrated Diving Systems | How do the local models interact across a complete dive profile? | 14–18 |

### Part I — Physics of Diving

Part I builds the physical causal chain before introducing formal systems language.

| Chapter | Companion notebook | New curriculum block | Principal outcome |
|:--|:--|:--|:--|
| 1. Pressure and Depth | 01 — Depth and Pressure | Depth → pressure | Derive and evaluate hydrostatic absolute pressure. |
| 2. Compressible Gases | 02 — Boyle's Law | Pressure → volume | Model nonlinear gas-volume change with depth. |
| 3. Archimedes' Principle | 03 — Archimedes' Principle | Volume → buoyant force | Derive buoyancy and neutral-displacement conditions. |
| 4. Buoyancy and Vertical Dynamics | 04 — Vertical Forces and Motion | Force → motion | Form the coupled nonlinear equations for depth and velocity. |

### Part II — Dynamical Systems

Part II reorganizes the physical model around state, local behavior, measurements, and uncertainty.

| Chapter | Companion notebook | New curriculum block | Principal outcome |
|:--|:--|:--|:--|
| 5. State-Space Models | 05 — State-Space Models | Motion → state | Construct and simulate a nonlinear state-space model. |
| 6. Equilibria and Stability | 06 — Equilibria and Stability | State → local behavior | Linearize the model and classify equilibria from eigenvalues. |
| 7. Observability and State Estimation | 07 — Observability and State Estimation | Measurements → estimated state | Test observability and design a Luenberger observer. |
| 8. Kalman Filtering | 08 — Kalman Filtering | Uncertainty → probabilistic estimate | Implement prediction and correction with explicit covariance. |

### Part III — Control Engineering

Part III changes the central question from predicting motion to shaping it.

| Chapter | Companion notebook | New curriculum block | Principal outcome |
|:--|:--|:--|:--|
| 9. Laplace Transforms and Transfer Functions | 09 — Laplace Transforms and Transfer Functions | Differential model → transfer function | Connect state-space poles, transfer functions, and responses. |
| 10. Feedback Control | 10 — Feedback Control | Estimate/error → control action | Design local depth and velocity feedback. |
| 11. PID Control | 11 — PID Control | Feedback → offset rejection | Interpret PID action, windup, noise, and tuning trade-offs. |
| 12. Frequency Response | 12 — Frequency Response | Time response → frequency behavior | Read Bode plots, resonance, bandwidth, and delay phase. |
| 13. The Diver in the Loop | 13 — Human-in-the-Loop Control | Automatic → human feedback | Model sampled decisions, delay, thresholds, and saturation. |

### Part IV — Integrated Diving Systems

Part IV applies the modeling vocabulary to interacting subsystems. These models remain educational and are not operational planning tools.

| Chapter | Companion notebook | New curriculum block | Principal outcome |
|:--|:--|:--|:--|
| 14. Breathing Dynamics | 14 — Breathing Dynamics | Breathing → buoyancy disturbance/control | Model bounded lung-volume actuation and phase lag. |
| 15. Gas Consumption | 15 — Gas Consumption | Depth/workload → gas-resource state | Integrate conditional gas demand over a profile. |
| 16. Dive Computers | 16 — Dive-Computer Estimation Pipeline | Sensors → information pipeline | Separate measured, derived, estimated, and predicted quantities. |
| 17. Decompression Models | 17 — Inert-Gas Compartment Models | Pressure history → hidden compartment states | Propagate simplified inert-gas states and delimit their meaning. |
| 18. The Complete Dive | 18 — Integrated DiveLab Capstone | Subsystems → integrated model | Reconstruct the full causal architecture and its uncertainties. |

---

## 5. Dependency path

The default route is sequential. The most important dependencies are:

- Chapters 1–4 establish the physical plant used throughout the book.
- Chapters 5–6 provide the state-space and stability language needed by estimation and control.
- Chapter 7 introduces deterministic observation before Chapter 8 adds stochastic estimation.
- Chapter 9 provides the transfer-function language used in Chapters 10–12.
- Chapter 13 combines the feedback concepts with human delay and intermittent action.
- Chapters 14–17 reuse selected earlier models as application subsystems.
- Chapter 18 assumes the complete sequence and serves as the integrative capstone.

Chapter-level prerequisite lines in the manuscript specify the exact local requirements.

---

## 6. Curriculum boundaries

DiveLab models are deliberately simplified to expose engineering structure. The curriculum does not provide:

- practical diving instruction or certification;
- operational gas, ascent, or decompression planning;
- medical or physiological advice;
- equipment qualification or safety certification;
- validated predictions for a particular diver or dive.

The appropriate learning outcome is better systems reasoning: knowing what a model contains, what it omits, how uncertainty enters, and what evidence would be required before using a model beyond the classroom.
