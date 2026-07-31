# DiveLab Architecture

> **The book explains. The notebooks experiment. The Python package implements.**

DiveLab is an open-source executable engineering textbook that uses scuba diving as a laboratory for physics, scientific computing, dynamic systems, simulation, and control.

This document defines the architectural structure of the project, the responsibilities of its main components, and the rules that should keep the codebase coherent as DiveLab grows.

---

# 1. Architectural Goals

The architecture should support five goals:

1. keep the student experience simple;
2. separate educational narrative from reusable software;
3. avoid duplicating mature logic across notebooks;
4. make simulations reproducible and testable;
5. allow DiveLab to evolve from a collection of labs into a reusable engineering framework.

The architecture should remain lightweight during V1 and grow only when new requirements justify additional complexity.

---

# 2. Core Design Principle

DiveLab is organized into four primary layers:

```text
                 DIVELAB
                    │
        ┌───────────┴───────────┐
        │                       │
      BOOK                   LABS
     Quarto              Jupyter/Colab
        │                       │
        └───────────┬───────────┘
                    │
                 divelab
              Python package
                    │
        ┌───────────┴───────────┐
        │                       │
      MODELS                DATA
 physics / dynamics      scenarios /
 simulation / control    parameters
```

Each layer has a distinct responsibility.

---

# 3. Curriculum and Engine

DiveLab should be understood as two connected subsystems.

```text
                 DiveLab
                    │
        ┌───────────┴───────────┐
        │                       │
   CURRICULUM                ENGINE
        │                       │
 Book + Labs              divelab package
        │                       │
 learning path             reusable models
```

## Curriculum

The curriculum contains the teaching experience:

- Quarto chapters;
- Jupyter/Colab notebooks;
- exercises;
- challenges;
- explanations;
- visualizations;
- learning progression.

Its primary concern is pedagogy.

## Engine

The engine contains reusable computational components:

- physical models;
- gas models;
- buoyancy models;
- dynamic models;
- simulation utilities;
- controllers;
- scenario loading;
- shared numerical tools.

Its primary concern is correctness, reuse, and testability.

The curriculum may depend on the engine.

The engine must never depend on the curriculum.

---

# 4. Repository Structure

The target repository structure is:

```text
divelab/
│
├── README.md
├── ROADMAP.md
├── ARCHITECTURE.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── _quarto.yml
│
├── book/
│   ├── index.qmd
│   ├── understand/
│   ├── model/
│   ├── simulate/
│   └── control/
│
├── notebooks/
│   ├── 01_understand/
│   ├── 02_model/
│   ├── 03_simulate/
│   └── 04_control/
│
├── src/
│   └── divelab/
│       ├── physics/
│       ├── gas/
│       ├── buoyancy/
│       ├── dynamics/
│       ├── simulation/
│       ├── control/
│       └── utils/
│
├── scenarios/
├── data/
├── figures/
├── tests/
├── scripts/
│
└── .github/
    └── workflows/
```

The exact internal subdivision may evolve, but the separation of responsibilities should remain stable.

---

# 5. Layer Responsibilities

## 5.1 Book Layer

Location:

```text
book/
```

Technology:

- Quarto;
- Markdown / `.qmd`;
- mathematical notation;
- static and generated figures;
- links to executable notebooks.

Responsibilities:

- explain concepts;
- provide the didactic narrative;
- introduce equations;
- connect physical intuition to mathematical models;
- point readers to executable labs;
- summarize interpretations and conclusions.

The book should not contain large amounts of unique computational logic.

Whenever possible, computational examples should either:

- call reusable functions from `divelab`; or
- mirror code intentionally introduced in a teaching notebook.

---

## 5.2 Notebook Layer

Location:

```text
notebooks/
```

Technology:

- Jupyter notebooks;
- Google Colab as the primary student runtime.

Responsibilities:

- experimentation;
- executable examples;
- visualization;
- parameter variation;
- discovery;
- exercises and challenges;
- progressive introduction of Python and modeling techniques.

A typical notebook should follow:

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

Notebook code should optimize for readability and learning, not abstraction.

However, mature reusable logic should eventually move into the package.

---

# 6. Python Package

Location:

```text
src/divelab/
```

The package is the computational core of DiveLab.

Suggested top-level structure:

```text
src/divelab/
├── physics/
├── gas/
├── buoyancy/
├── dynamics/
├── simulation/
├── control/
└── utils/
```

The modules should remain small and concept-oriented during V1.

---

## 6.1 Physics Module

Location:

```text
src/divelab/physics/
```

Responsibilities:

- hydrostatic pressure;
- absolute and gauge pressure;
- Boyle's law;
- density-related calculations;
- Archimedes' principle;
- physical constants where appropriate.

Possible examples:

```python
pressure_at_depth(...)
absolute_pressure(...)
gas_volume_at_pressure(...)
buoyant_force(...)
```

The module should contain general physical relationships rather than diver-specific behavior whenever possible.

---

## 6.2 Gas Module

Location:

```text
src/divelab/gas/
```

Responsibilities:

- tank gas calculations;
- surface air consumption;
- depth-adjusted consumption;
- gas availability;
- gas use over time;
- gas-related parameters.

Possible examples:

```python
available_gas(...)
ambient_consumption_rate(...)
gas_used(...)
remaining_gas(...)
```

---

## 6.3 Buoyancy Module

Location:

```text
src/divelab/buoyancy/
```

Responsibilities:

- diver buoyancy;
- equipment buoyancy;
- BCD gas volume;
- exposure suit compression;
- weighting;
- net buoyancy.

Possible examples:

```python
bcd_buoyancy(...)
suit_buoyancy(...)
net_buoyancy(...)
```

The exact physical fidelity can evolve over time.

V1 should prefer transparent models over unnecessary realism.

---

## 6.4 Dynamics Module

Location:

```text
src/divelab/dynamics/
```

Responsibilities:

- state representation;
- vertical motion;
- force balance;
- simplified drag;
- acceleration;
- state derivatives.

A generic model can follow:

$$
\dot{x} = f(x,u,t)
$$

Possible state variables may include:

```text
depth
vertical_velocity
gas_remaining
bcd_gas
```

The state should remain minimal for each educational stage.

---

## 6.5 Simulation Module

Location:

```text
src/divelab/simulation/
```

Responsibilities:

- time integration;
- simulation loop;
- trajectory generation;
- scenario execution;
- output collection;
- simulation result structures.

Conceptually:

```python
result = simulate(model, scenario)
```

A simulation should clearly distinguish:

- model;
- initial state;
- parameters;
- inputs;
- disturbances;
- time configuration.

---

## 6.6 Control Module

Location:

```text
src/divelab/control/
```

Responsibilities:

- feedback controllers;
- proportional control;
- PID control;
- target tracking;
- controller state where necessary.

A controller should conceptually follow:

```python
control_input = controller(target, observed_state, time)
```

The control module should depend on model interfaces rather than notebook code.

---

## 6.7 Utilities Module

Location:

```text
src/divelab/utils/
```

This module should remain small.

It may contain reusable helpers that do not naturally belong elsewhere, such as:

- validation;
- unit-related helpers;
- shared numerical utilities;
- formatting support.

It should not become a generic dumping ground.

---

# 7. Scenarios

Location:

```text
scenarios/
```

Scenarios describe experiments without embedding simulation logic.

Examples:

```text
open_water_18m.yaml
deep_dive_30m.yaml
ascent_18m.yaml
buoyancy_failure.yaml
```

A scenario may eventually contain:

```yaml
name: open_water_18m

diver:
  mass_kg: 80

tank:
  volume_l: 12
  pressure_bar: 200

profile:
  target_depth_m: 18
  bottom_time_min: 20

environment:
  water: salt
```

Scenario files should contain parameters and configuration, not executable code.

---

# 8. Data

Location:

```text
data/
```

The data directory is intended for:

- reference datasets;
- synthetic dive data;
- example logs;
- calibration data;
- future real-world datasets that can legally and safely be distributed.

Data should not be mixed with scenario definitions.

The distinction is:

```text
scenario = what should happen
data     = what was observed or supplied
```

---

# 9. Figures

Location:

```text
figures/
```

Use this directory for:

- reusable diagrams;
- exported plots;
- book illustrations;
- architecture figures.

Generated figures should be reproducible whenever practical.

Large generated outputs should not be committed unless they are needed for publication or reproducibility.

---

# 10. Tests

Location:

```text
tests/
```

The reusable Python package should be testable independently from the notebooks.

Tests should initially focus on:

- known physical relationships;
- units and signs;
- boundary conditions;
- expected simulation behavior;
- controller sanity checks.

Example categories:

```text
tests/
├── test_physics.py
├── test_gas.py
├── test_buoyancy.py
├── test_dynamics.py
├── test_simulation.py
└── test_control.py
```

Educational notebooks do not replace automated tests.

---

# 11. Scripts

Location:

```text
scripts/
```

Scripts are intended for project maintenance and generation tasks, such as:

- notebook validation;
- notebook execution;
- figure generation;
- scenario validation;
- build helpers.

Reusable domain logic should not live in `scripts/`.

---

# 12. Dependency Direction

Dependencies should flow downward toward reusable computational components.

```text
Book
 ↓
Notebooks
 ↓
DiveLab package
 ↓
Models / utilities
```

More precisely:

```text
book ---------> divelab
  \               ↑
   \              |
    -> notebooks --+
```

Allowed:

- book → package;
- notebook → package;
- simulation → dynamics;
- control → shared model abstractions;
- package → standard scientific Python libraries.

Avoid:

- package → notebooks;
- package → book;
- model modules → visualization code;
- core physics → control;
- circular dependencies.

---

# 13. Notebook-to-Package Evolution

DiveLab should not prematurely move every formula into a library.

During early teaching, explicit implementation is valuable.

For example, a student may first write:

```python
pressure_bar = 1 + depth_m / 10
```

Later notebooks may use:

```python
from divelab.physics import pressure_at_depth
```

The evolution should be:

```text
teach explicitly
      ↓
use repeatedly
      ↓
identify stable abstraction
      ↓
move to divelab package
      ↓
test
      ↓
reuse
```

This preserves educational transparency while avoiding long-term duplication.

---

# 14. Model Design Principles

## Transparency before realism

V1 models should be understandable.

A simpler model with explicit assumptions is preferable to a realistic model whose behavior cannot easily be explained.

## Assumptions must be visible

Every model should document its assumptions.

For example:

```text
Assumption:
1 bar increase every 10 m of seawater depth.
```

Later versions may introduce higher-fidelity formulations.

## Units must be explicit

Functions should make expected units clear in names, documentation, or typed structures.

Examples:

```python
depth_m
pressure_bar
volume_l
time_s
mass_kg
```

Avoid silently mixing unit systems.

## Pure functions where practical

For foundational calculations, prefer functions where output depends only on explicit inputs.

This improves:

- reproducibility;
- testing;
- educational clarity.

Stateful objects should be introduced only when they simplify dynamic or control models.

---

# 15. State, Parameters, Inputs, and Disturbances

Dynamic modeling should consistently distinguish four concepts.

## State

Variables that evolve over time.

Example:

```text
depth
vertical velocity
gas remaining
```

## Parameters

Values that characterize the system and normally remain fixed during one simulation.

Example:

```text
diver mass
tank capacity
drag coefficient
```

## Inputs

Actions applied to the system.

Example:

```text
BCD inflation
BCD dump
finning effort
```

## Disturbances

External effects that are not directly commanded.

Example:

```text
current
unexpected buoyancy shift
equipment change
```

This distinction should be reused throughout the Model, Simulate, and Control curriculum.

---

# 16. Simulation Architecture

A simulation should conceptually combine:

```text
Scenario
   │
   ├── Initial state
   ├── Parameters
   ├── Environment
   └── Profile
          │
          ↓
        Model
          │
          ↓
      Simulator
          │
          ↓
        Result
```

A future API might look like:

```python
scenario = load_scenario("open_water_18m")

result = simulate(
    model=diver_model,
    scenario=scenario,
)
```

Simulation results should be easy to inspect and visualize.

---

# 17. Control Architecture

The control layer should build on the simulation layer.

```text
           target
              │
              ↓
         controller
              │
              ↓
            input
              │
              ↓
            model
              │
              ↓
            state
              │
              └──────── feedback
```

The same underlying diver model should ideally support both:

- uncontrolled simulation;
- controlled simulation.

This makes feedback effects directly comparable.

---

# 18. Quarto and Colab

Quarto and Colab serve different roles.

## Quarto

Primary role:

```text
structured textbook
```

It organizes the complete learning journey and supports publication.

## Colab

Primary role:

```text
interactive laboratory
```

It gives students a zero-install execution environment.

Each important lab should eventually have a clear launch path from the book to Colab.

The repository remains the source of truth.

---

# 19. Versioning Strategy

During V1:

- prioritize conceptual completeness;
- avoid unnecessary API stability guarantees;
- keep interfaces simple;
- document breaking changes when needed.

After V1, the reusable Python package can adopt stronger semantic versioning practices.

Suggested milestone:

```text
0.x  → curriculum and engine evolving
1.0  → first coherent public architecture
```

The book release and Python package version do not necessarily need to evolve at exactly the same cadence.

---

# 20. Continuous Integration

The initial CI workflow should remain lightweight.

It may eventually verify:

- Python tests;
- package importability;
- notebook syntax or execution;
- Quarto build;
- broken links;
- scenario validity.

A minimal dependency flow is:

```text
push / pull request
        │
        ↓
   install project
        │
        ↓
      tests
        │
        ↓
   Quarto build
```

More expensive notebook execution can be added incrementally.

---

# 21. Architectural Rules

The following rules summarize the intended architecture.

### Rule 1

The repository is the source of truth.

### Rule 2

The book teaches concepts.

### Rule 3

The notebooks provide experiments.

### Rule 4

The package contains reusable computational logic.

### Rule 5

Scenarios contain configuration, not executable logic.

### Rule 6

Data and scenarios are different concepts.

### Rule 7

Reusable models must be testable independently from notebooks.

### Rule 8

Dependencies should flow toward the computational core.

### Rule 9

Prefer transparent models before high-fidelity models.

### Rule 10

Complete the V1 learning path before substantial V2 redesign.

---

# 22. Architecture Evolution

The architecture should evolve progressively.

## V1

Focus on:

- physics;
- models;
- simulation;
- feedback;
- coherent textbook;
- reusable core functions;
- simple scenario mechanism.

## V2 and beyond

Possible architectural extensions include:

- richer typed configuration models;
- interactive widgets;
- web simulation front ends;
- automated assessment;
- real dive-computer data import;
- parameter estimation;
- optimization;
- uncertainty analysis;
- advanced physiological models;
- richer controller libraries;
- instructor dashboards.

These should be added only when they support concrete learning or engineering goals.

---

# 23. Architectural North Star

A learner should eventually be able to write code such as:

```python
from divelab.simulation import simulate
from divelab.scenarios import load_scenario

scenario = load_scenario("open_water_18m")
result = simulate(scenario)

result.plot_depth()
```

and later:

```python
from divelab.control import PIDController

controller = PIDController(...)
result = simulate(scenario, controller=controller)
```

while still understanding the physical equations and computational models that make those abstractions possible.

That balance between **understanding and abstraction** is the central architectural principle of DiveLab.
