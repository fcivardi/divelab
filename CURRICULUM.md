# DiveLab Curriculum

> **Understand → Model → Simulate → Control**

DiveLab is an open-source executable engineering textbook that uses scuba diving as a laboratory for physics, scientific computing, dynamic systems, simulation, and control.

This document defines the **DiveLab V1 curriculum**: the sequence of learning modules and notebooks, their objectives, dependencies, experiments, and expected outcomes.

It complements:

- `ROADMAP.md` — what is built and in which order;
- `ARCHITECTURE.md` — how the project components are organized;
- `CURRICULUM.md` — what the learner studies and in which sequence.

---

# 1. Curriculum Goals

DiveLab V1 should guide a learner from intuitive physical reasoning to a simplified feedback-controlled model of a scuba diver.

The progression is:

```text
UNDERSTAND
Physics and intuition
      ↓
MODEL
Equations and computational models
      ↓
SIMULATE
Time evolution and scenarios
      ↓
CONTROL
Feedback and stability
```

At the end of V1, the learner should be able to:

1. explain the main physical relationships relevant to diving;
2. translate those relationships into mathematical models;
3. implement and explore the models in Python;
4. distinguish states, parameters, inputs, and disturbances;
5. simulate a simplified dive over time;
6. visualize and interpret simulation results;
7. understand open-loop and closed-loop behavior;
8. implement a basic feedback controller;
9. reason about a diver as a dynamic system.

---

# 2. Intended Audience

DiveLab is designed for learners interested in combinations of:

- scuba diving;
- physics;
- engineering;
- Python;
- scientific computing;
- mathematical modeling;
- simulation;
- control systems.

The V1 curriculum should not require advanced control theory or advanced numerical analysis at the beginning.

Basic familiarity with algebra is useful.

Python is introduced through the experiments rather than treated as a separate prerequisite course.

---

# 3. Learning Philosophy

Each notebook should begin with a meaningful question.

The preferred learning cycle is:

```text
Question
   ↓
Physical intuition
   ↓
Mathematical model
   ↓
Python implementation
   ↓
Experiment
   ↓
Visualization
   ↓
Interpretation
   ↓
Challenge
```

The objective is not simply to calculate correct numbers.

The learner should progressively develop the habit of asking:

```text
What is the system?
What variables matter?
What assumptions are we making?
What changes when a parameter changes?
What happens over time?
Can we predict the behavior?
Can we control it?
```

---

# 4. Curriculum Structure

DiveLab V1 contains four main parts.

| Part | Theme | Main Question |
|---|---|---|
| I | Understand | What happens underwater? |
| II | Model | How can we represent it mathematically? |
| III | Simulate | How does the system evolve over time? |
| IV | Control | How can feedback influence the behavior? |

The initial target is approximately **16 core notebooks**, with optional extension labs added only after the V1 path is coherent.

---

# Part I — UNDERSTAND

## Physics of Diving

The first part builds intuition and quantitative reasoning.

The learner should understand the physical mechanisms before they are hidden behind reusable abstractions.

---

## Notebook 01 — Depth and Pressure

### Guiding question

**How does pressure change as a diver descends?**

### Concepts

- depth;
- surface pressure;
- hydrostatic pressure;
- absolute pressure;
- gauge pressure;
- seawater approximation.

### Mathematical model

A first approximation:

$$
P_{\mathrm{abs}} \approx 1 + \frac{d}{10}
$$

with pressure in bar and depth in meters.

### Python skills

- variables;
- arithmetic expressions;
- functions;
- NumPy arrays;
- simple plots.

### Experiment

Calculate and plot pressure from the surface to recreational diving depths.

### Challenge

Compare pressure changes over equal depth intervals and explain why depth is not proportional to relative pressure change.

### Outcome

The learner can calculate and visualize ambient pressure as a function of depth.

### Dependency

None.

---

## Notebook 02 — Boyle's Law and Gas Volume

### Guiding question

**Why do gas volumes change so dramatically near the surface?**

### Concepts

- pressure-volume relationship;
- Boyle's law;
- compression;
- expansion;
- relative versus absolute changes.

### Mathematical model

$$
P_1 V_1 = P_2 V_2
$$

### Python skills

- reusable functions;
- vectorized calculations;
- plotting nonlinear relationships.

### Experiment

Track the volume of a flexible gas space during descent and ascent.

### Challenge

Compare the volume change from 30 m to 20 m with the change from 10 m to the surface.

### Outcome

The learner connects pressure changes to gas-volume changes and recognizes the nonlinear significance of the shallowest part of the water column.

### Dependency

Notebook 01.

---

## Notebook 03 — Buoyancy and Archimedes

### Guiding question

**Why does an object float, sink, or remain neutrally buoyant?**

### Concepts

- mass;
- weight;
- displaced water;
- density;
- buoyant force;
- positive, negative, and neutral buoyancy.

### Mathematical model

$$
F_B = \rho g V
$$

and:

$$
F_{\mathrm{net}} = F_B - mg
$$

### Python skills

- functions with physical parameters;
- comparisons;
- tables;
- parameter sweeps.

### Experiment

Compare objects with different mass and displaced volume.

### Challenge

Find the displaced volume required for neutral buoyancy for a given mass.

### Outcome

The learner can calculate net buoyancy and explain neutral buoyancy quantitatively.

### Dependency

Notebook 01.

---

## Notebook 04 — The Diver as a Buoyancy System

### Guiding question

**Why does a diver's buoyancy change during a dive?**

### Concepts

- diver mass;
- equipment;
- exposure suit;
- BCD;
- gas spaces;
- weighting;
- depth-dependent compression.

### Python skills

- decomposition of a system into components;
- structured parameters;
- sensitivity plots.

### Experiment

Build a simplified buoyancy budget and vary depth, weighting, suit volume, and BCD gas.

### Challenge

Determine what BCD volume would restore neutral buoyancy after a modeled change.

### Outcome

The learner sees the diver as a system of interacting buoyancy components rather than as a single object.

### Dependencies

Notebooks 02 and 03.

---

# Part II — MODEL

## From Physical Laws to Computational Models

Part II moves from isolated equations to explicit models of a diver and equipment.

The key conceptual transition is:

```text
formula
   ↓
component
   ↓
system
   ↓
model
```

---

## Notebook 05 — Gas Supply and Consumption

### Guiding question

**How does depth affect how quickly a diver uses the available gas supply?**

### Concepts

- cylinder volume;
- cylinder pressure;
- available surface-equivalent gas;
- surface air consumption;
- ambient pressure;
- depth-dependent gas use.

### Python skills

- model functions;
- parameter validation;
- plotting multiple scenarios.

### Experiment

Compare gas consumption at several depths for the same surface consumption rate.

### Challenge

Estimate remaining gas after a simplified bottom segment.

### Outcome

The learner can model available gas and consumption as functions of time and ambient pressure.

### Dependencies

Notebooks 01 and 02.

---

## Notebook 06 — Building a Diver Model

### Guiding question

**What information is needed to represent a diver computationally?**

### Concepts

- system boundary;
- parameters;
- derived quantities;
- model assumptions;
- simplification.

### Candidate parameters

```text
diver mass
equipment mass
displaced volume
suit characteristics
BCD characteristics
tank characteristics
gas consumption rate
```

### Python skills

- dictionaries or dataclasses;
- structured models;
- separation of parameters and calculations.

### Experiment

Create several diver configurations and compare their predicted properties.

### Challenge

Identify which parameters are fundamental and which can be derived.

### Outcome

The learner can represent a simplified diver as a structured computational model.

### Dependencies

Notebooks 03, 04, and 05.

---

## Notebook 07 — States, Inputs, Parameters, Disturbances

### Guiding question

**Which quantities describe the system, and which quantities cause it to change?**

### Concepts

- state;
- input;
- parameter;
- disturbance;
- observation;
- initial condition.

### Example classification

```text
depth              → state
vertical velocity  → state
BCD action         → input
diver mass         → parameter
current            → disturbance
```

### Python skills

- state structures;
- state updates;
- explicit model interfaces.

### Experiment

Classify and manipulate the variables in a simplified diver model.

### Challenge

Reclassify variables under alternative modeling assumptions and explain the choices.

### Outcome

The learner understands the vocabulary needed for dynamic systems and control.

### Dependency

Notebook 06.

---

## Notebook 08 — Vertical Forces and Motion

### Guiding question

**What makes a diver accelerate upward or downward?**

### Concepts

- net force;
- buoyancy;
- weight;
- drag;
- acceleration;
- velocity;
- depth convention.

### Mathematical model

$$
m a = \sum F
$$

with a simplified vertical force balance.

### Python skills

- force functions;
- sign conventions;
- incremental state updates;
- diagnostic plots.

### Experiment

Calculate acceleration under different buoyancy and velocity conditions.

### Challenge

Find conditions that produce approximately constant vertical velocity in the simplified model.

### Outcome

The learner connects buoyancy calculations to motion.

### Dependencies

Notebooks 04 and 07.

---

# Part III — SIMULATE

## From Models to Time Evolution

Part III introduces the central idea that a system has a state that evolves.

```text
x(t)
```

and, conceptually:

$$
\dot{x} = f(x,u,t)
$$

---

## Notebook 09 — Time-Stepping a Dynamic System

### Guiding question

**How can a computer approximate continuous motion?**

### Concepts

- continuous versus discrete time;
- time step;
- numerical approximation;
- Euler integration;
- accumulated numerical error.

### Python skills

- loops;
- arrays;
- state history;
- time-series plots.

### Experiment

Simulate a simple one-dimensional dynamic system with different time steps.

### Challenge

Compare results for multiple values of `dt`.

### Outcome

The learner understands the basic mechanism of numerical simulation.

### Dependency

Notebook 08.

---

## Notebook 10 — Simulating Descent and Ascent

### Guiding question

**Can the vertical motion of a diver be simulated over time?**

### Concepts

- initial state;
- dynamic force balance;
- velocity;
- depth;
- drag;
- trajectory.

### Python skills

- simulation loops;
- state recording;
- multi-variable plots.

### Experiment

Simulate simplified descent and ascent trajectories.

### Challenge

Change buoyancy and drag parameters and interpret the resulting trajectories.

### Outcome

The learner can simulate the vertical motion of a simplified diver.

### Dependencies

Notebooks 08 and 09.

---

## Notebook 11 — Gas Consumption Over a Dive Profile

### Guiding question

**How does a changing depth profile affect gas consumption?**

### Concepts

- time-dependent depth;
- ambient pressure;
- consumption rate;
- cumulative gas use;
- remaining gas.

### Python skills

- combining models;
- interpolation or piecewise profiles;
- cumulative calculations.

### Experiment

Simulate gas consumption during descent, bottom phase, and ascent.

### Challenge

Compare two profiles with similar duration but different depth histories.

### Outcome

The learner integrates pressure, gas, and time into one simulation.

### Dependencies

Notebooks 05, 09, and 10.

---

## Notebook 12 — Scenario-Based Dive Simulation

### Guiding question

**Can we describe a dive as a scenario and run it reproducibly?**

### Concepts

- scenario;
- configuration;
- initial conditions;
- environment;
- reproducibility;
- simulation outputs.

### Candidate scenarios

```text
open_water_18m
deep_dive_30m
ascent_18m
buoyancy_change
```

### Python skills

- structured configuration;
- reusable simulation functions;
- result objects;
- comparison of runs.

### Experiment

Run multiple scenarios through the same simulation engine.

### Challenge

Create a new scenario by changing only configuration values, without modifying simulation logic.

### Outcome

The learner understands the separation between model, scenario, and simulator.

### Dependencies

Notebooks 10 and 11.

---

# Part IV — CONTROL

## Scuba Diving as a Feedback System

The final part reframes the diver as a controlled dynamic system.

```text
target
   ↓
controller
   ↓
diver
   ↓
depth
   └──── feedback
```

---

## Notebook 13 — Open Loop and Closed Loop

### Guiding question

**What changes when the system reacts to its own behavior?**

### Concepts

- open-loop control;
- closed-loop control;
- feedback;
- target;
- measurement;
- error.

### Python skills

- controller functions;
- comparison experiments;
- tracking-error plots.

### Experiment

Compare a predefined control action with a feedback-based action.

### Challenge

Introduce a disturbance and compare open-loop and closed-loop responses.

### Outcome

The learner understands why feedback can make a system more robust to uncertainty and disturbances.

### Dependencies

Notebooks 07, 10, and 12.

---

## Notebook 14 — Proportional Buoyancy Control

### Guiding question

**Can a simple feedback rule maintain a target depth?**

### Concepts

- depth error;
- proportional control;
- controller gain;
- response speed;
- oscillation;
- stability intuition.

### Control law

A simplified form:

$$
u = K_p e
$$

### Python skills

- feedback loops;
- parameter tuning;
- comparative plots.

### Experiment

Test several values of proportional gain.

### Challenge

Find gains that are too weak, useful, and excessively aggressive.

### Outcome

The learner sees how controller parameters change system behavior.

### Dependency

Notebook 13.

---

## Notebook 15 — PID Control

### Guiding question

**What do integral and derivative action add to proportional feedback?**

### Concepts

- proportional action;
- integral action;
- derivative action;
- steady-state error;
- damping intuition;
- tuning trade-offs.

### Control law

$$
u(t) =
K_p e(t)
+
K_i \int e(t)\,dt
+
K_d \frac{de(t)}{dt}
$$

### Python skills

- controller state;
- numerical integration of error;
- numerical derivative;
- tuning experiments.

### Experiment

Compare P, PI, and PID behavior in the simplified diver model.

### Challenge

Tune a controller for target-depth tracking while limiting oscillation.

### Outcome

The learner can implement and interpret a basic PID controller.

### Dependency

Notebook 14.

---

## Notebook 16 — Integrated DiveLab Challenge

### Guiding question

**Can we combine physics, modeling, simulation, and control into one experiment?**

### Concepts

This capstone combines the entire V1 path:

- pressure;
- gas;
- buoyancy;
- diver parameters;
- dynamic state;
- simulation;
- disturbances;
- feedback;
- performance evaluation.

### Experiment

Construct a simplified controlled dive scenario.

For example:

```text
surface
   ↓
controlled descent
   ↓
target depth
   ↓
depth holding
   ↓
disturbance
   ↓
recovery
   ↓
controlled ascent
```

### Python skills

- composition of modules;
- scenario definition;
- simulation;
- visualization;
- performance metrics;
- interpretation.

### Challenge

Modify one part of the system and defend the engineering choice using simulation results.

### Outcome

The learner demonstrates the complete DiveLab learning progression:

```text
Understand → Model → Simulate → Control
```

### Dependencies

All previous core notebooks.

---

# 5. Notebook Dependency Map

The main path is intentionally close to linear, while allowing some parallel development.

```text
01 Depth & Pressure
├── 02 Boyle's Law
│   └── 04 Diver Buoyancy System
│
├── 03 Archimedes
│   └── 04 Diver Buoyancy System
│
└── 05 Gas Supply & Consumption

04 + 05
   ↓
06 Diver Model
   ↓
07 State / Input / Parameter / Disturbance
   ↓
08 Vertical Forces & Motion
   ↓
09 Time Stepping
   ↓
10 Descent & Ascent
   ├── 11 Gas Over Dive Profile
   │
   └────────┐
            ↓
12 Scenario-Based Simulation
   ↓
13 Open vs Closed Loop
   ↓
14 Proportional Control
   ↓
15 PID Control
   ↓
16 Integrated Challenge
```

---

# 6. Python Learning Progression

DiveLab teaches Python progressively through engineering problems.

| Stage | Python concepts |
|---|---|
| Understand | variables, arithmetic, functions, arrays, plots |
| Model | structured data, reusable functions, model decomposition |
| Simulate | loops, state histories, numerical integration |
| Control | feedback functions, controller state, tuning experiments |
| Capstone | module composition, scenarios, result analysis |

Python should remain a tool for scientific reasoning rather than becoming a separate programming syllabus.

---

# 7. Mathematical Progression

The mathematical complexity should also increase progressively.

### Stage 1 — Algebraic relationships

Examples:

$$
P = f(d)
$$

$$
P_1V_1=P_2V_2
$$

$$
F_B=\rho gV
$$

### Stage 2 — System models

Examples:

$$
F_{\mathrm{net}} = F_B - W - F_D
$$

### Stage 3 — Dynamic models

Conceptually:

$$
\dot{x}=f(x,u,t)
$$

### Stage 4 — Feedback control

$$
e(t)=r(t)-y(t)
$$

and:

$$
u(t)=K_p e(t)
$$

followed by PID control.

The learner should encounter each mathematical abstraction only after its physical meaning has been established.

---

# 8. Notebook V1 Definition of Done

A core V1 notebook is complete when it contains:

- a clear guiding question;
- stated learning objectives;
- required prior knowledge;
- physical intuition;
- explicit assumptions;
- mathematical model;
- executable Python code;
- at least one visualization where meaningful;
- an experiment;
- interpretation questions;
- at least one challenge;
- a concise summary;
- a Colab-compatible execution path.

A notebook should not be considered complete merely because the code runs.

---

# 9. Scientific Modeling Policy

DiveLab is an educational engineering project.

Models should distinguish clearly between:

- physical law;
- engineering approximation;
- pedagogical simplification;
- empirical parameter;
- simulation assumption.

Where a model is simplified, the simplification should be explicit.

DiveLab should not present simplified educational simulations as operational dive-planning tools.

The curriculum should prioritize understanding and model transparency over false precision.

---

# 10. Core vs Extension Labs

The 16 notebooks above define the initial **core V1 path**.

Additional labs may later be added as extensions without blocking V1.

Possible extensions include:

- freshwater versus seawater;
- gas density at depth;
- alternative cylinder configurations;
- sensitivity analysis;
- uncertainty;
- Monte Carlo simulation;
- optimization;
- sensor noise;
- parameter estimation;
- dive-computer data;
- more advanced controllers;
- physiological models where scientifically appropriate.

Extension labs should connect to the core curriculum rather than fragment it.

---

# 11. Relationship to the Repository

The curriculum maps to the repository as follows:

```text
notebooks/
├── 01_understand/
│   ├── 01_depth_pressure.ipynb
│   ├── 02_boyles_law.ipynb
│   ├── 03_archimedes.ipynb
│   └── 04_diver_buoyancy.ipynb
│
├── 02_model/
│   ├── 05_gas_consumption.ipynb
│   ├── 06_diver_model.ipynb
│   ├── 07_state_input_parameter.ipynb
│   └── 08_vertical_dynamics.ipynb
│
├── 03_simulate/
│   ├── 09_time_stepping.ipynb
│   ├── 10_descent_ascent.ipynb
│   ├── 11_gas_profile.ipynb
│   └── 12_scenarios.ipynb
│
└── 04_control/
    ├── 13_feedback.ipynb
    ├── 14_proportional_control.ipynb
    ├── 15_pid_control.ipynb
    └── 16_integrated_challenge.ipynb
```

The Quarto book should mirror this conceptual structure without being forced to reproduce notebook content verbatim.

---

# 12. Curriculum Milestones

| Milestone | Curriculum outcome |
|---|---|
| C1 | Learner understands pressure, gas volume, and buoyancy |
| C2 | Learner can build a simplified computational diver model |
| C3 | Learner understands state and vertical dynamics |
| C4 | Learner can simulate a dive trajectory and gas use |
| C5 | Learner understands feedback and proportional control |
| C6 | Learner can experiment with PID control |
| C7 | Learner completes an integrated simulation and control challenge |

---

# 13. V1 Completion Criterion

DiveLab V1 curriculum is complete when a learner can begin with the question:

> **What happens to a diver underwater?**

and progressively reach the engineering question:

> **How can we model, simulate, and control the behavior of this dynamic system?**

The complete path should make the transition visible:

```text
physical phenomenon
        ↓
     equation
        ↓
      model
        ↓
    simulation
        ↓
     feedback
        ↓
     control
```

That progression is the educational backbone of DiveLab.
