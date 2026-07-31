# DiveLab Roadmap

> **Understand → Model → Simulate → Control**

DiveLab is an open-source executable engineering textbook that uses scuba diving as a laboratory for physics, scientific computing, dynamic systems, simulation, and control.

This roadmap defines the path to **DiveLab V1**: a coherent end-to-end learning experience built around Python, Jupyter/Google Colab, and Quarto.

## 1. Goals

DiveLab V1 should:

- provide a coherent path from physical intuition to feedback control;
- combine explanations, mathematical models, Python experiments, and simulations;
- run student-facing labs in Google Colab without requiring local installation;
- separate educational content from reusable software components;
- support publication as a Quarto book;
- establish a stable foundation for DiveLab V2.

The learning progression is:

1. **Understand** — build physical intuition.
2. **Model** — translate phenomena into mathematical and computational models.
3. **Simulate** — study how systems evolve over time.
4. **Control** — introduce feedback, stability, and control engineering.

## 2. Development Principles

### Complete V1 before V2

Complete a coherent end-to-end V1 before substantially redesigning existing notebooks. V1 validates the curriculum, architecture, and learning progression; V2 will focus on refinement and richer interaction.

### Colab-first

Student-facing notebooks should run in Google Colab whenever practical. Students should not need to configure a local Python environment.

### Separate curriculum and engine

**Curriculum**
- Quarto book
- Jupyter/Colab labs
- exercises and challenges

**Engine**
- reusable Python models
- simulation utilities
- scenarios and parameters
- control components

The book explains, the notebooks experiment, and the Python package implements reusable functionality.

### Progressive complexity

A typical lab follows:

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

# 3. DiveLab V1 Roadmap

## Sprint 0 — Repository Bootstrap

**Goal:** Create a clean and reproducible project foundation.

### Deliverables

- repository structure;
- README;
- license;
- `ROADMAP.md`;
- `ARCHITECTURE.md`;
- Quarto configuration;
- Python project configuration;
- notebook conventions;
- basic CI workflow.

### Target structure

```text
divelab/
├── README.md
├── ROADMAP.md
├── ARCHITECTURE.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── _quarto.yml
├── book/
├── notebooks/
├── src/
├── scenarios/
├── data/
├── figures/
├── tests/
├── scripts/
└── .github/
    └── workflows/
```

### Definition of Done

- repository can be cloned successfully;
- documentation explains the purpose of DiveLab;
- a minimal Quarto book can be rendered;
- at least one notebook can be launched in Colab;
- project structure is stable enough for subsequent sprints.

## Sprint 1 — Physics Foundations

**Goal:** Build the physical foundations required to reason quantitatively about diving.

### Topics

- depth and pressure;
- absolute and gauge pressure;
- hydrostatic pressure;
- Boyle's law;
- gas volume changes;
- Archimedes' principle;
- buoyancy;
- basic gas consumption.

### Deliverables

- first sequence of V1 notebooks;
- corresponding book chapters;
- reusable pressure and basic physics functions where appropriate;
- exercises and interpretation questions.

### Definition of Done

Students can move from physical intuition to simple quantitative Python experiments without requiring knowledge of dynamic systems.

## Sprint 2 — Gas and Buoyancy Models

**Goal:** Move from isolated equations to reusable models of a diver and equipment.

### Topics

- gas density;
- tank pressure and available gas;
- surface air consumption;
- depth-dependent gas consumption;
- buoyancy components;
- BCD volume;
- exposure suit compression;
- weighting;
- buoyancy changes during a dive.

### Deliverables

- gas model;
- buoyancy model;
- parameterized diver/equipment examples;
- sensitivity experiments;
- initial reusable modules under `src/divelab/`.

### Definition of Done

A student can construct a simplified quantitative model of a diver and predict how depth and equipment parameters affect gas use and buoyancy.

## Sprint 3 — Dynamic Models

**Goal:** Introduce time and state.

DiveLab moves from static calculations to:

```text
state(t)
```

### Topics

- state variables;
- inputs;
- parameters;
- disturbances;
- vertical position and velocity;
- forces;
- simplified drag;
- dynamic buoyancy;
- descent and ascent models.

A general model can be introduced as:

$$
\dot{x} = f(x,u,t)
$$

### Deliverables

- first dynamic diver model;
- notebooks introducing state and evolution over time;
- numerical examples;
- reusable dynamics module.

### Definition of Done

Students understand the difference between a static calculation and a dynamic model and can identify states, inputs, parameters, and disturbances.

## Sprint 4 — Simulation

**Goal:** Turn dynamic models into executable dive simulations.

### Topics

- numerical integration;
- time steps;
- trajectories;
- descent;
- bottom phase;
- ascent;
- gas consumption over time;
- buoyancy evolution;
- disturbances;
- scenario-based simulation.

### Example scenarios

```text
open_water_18m
deep_dive_30m
ascent_18m
buoyancy_change
```

### Deliverables

- simulation engine;
- scenario format;
- end-to-end dive simulation;
- plots of depth, velocity, gas, and state variables;
- simulation notebooks.

### Definition of Done

A complete simplified dive profile can be simulated from initial conditions and parameters, producing interpretable time-series results.

## Sprint 5 — Feedback and Control

**Goal:** Use scuba diving to introduce control engineering.

```text
target depth
     ↓
   diver
     ↓
 buoyancy
     ↓
 vertical dynamics
     ↓
 actual depth
     ─────────┐
              │
          feedback
```

### Topics

- open-loop versus closed-loop behavior;
- target depth;
- error;
- feedback;
- stability;
- disturbances;
- proportional control;
- PID concepts;
- buoyancy control.

### Deliverables

- control-oriented diver model;
- feedback experiments;
- basic controller implementation;
- controlled versus uncontrolled comparisons;
- introductory PID notebook.

### Definition of Done

Students can explain why feedback is useful, implement a basic controller, and interpret its effect on a simulated diver.

## Sprint 6 — Book Integration

**Goal:** Transform individual labs and models into a coherent executable textbook.

### Deliverables

- complete Quarto navigation;
- four major parts: Understand, Model, Simulate, Control;
- consistent chapter structure;
- links between chapters and Colab notebooks;
- standardized figures and equations;
- glossary and references;
- developer documentation;
- student getting-started guide.

### Definition of Done

A new reader can start from the DiveLab home page and follow the entire V1 learning path without needing knowledge of the project's development history.

## Sprint 7 — DiveLab V1 Release

**Goal:** Prepare the first complete public release.

### Deliverables

- review and test all notebooks;
- verify Colab compatibility;
- test Quarto build;
- validate examples and simulations;
- run automated tests;
- clean repository and documentation;
- tag the V1 release;
- publish the executable book.

### Definition of Done

DiveLab V1 provides a complete learning journey:

```text
Understand → Model → Simulate → Control
```

and all core materials can be accessed, executed, and reproduced.

# 4. Beyond V1 — DiveLab V2

V2 begins only after the V1 learning path is complete.

Potential directions include:

- richer interactive widgets;
- improved visualization;
- automated exercises and assessment;
- more realistic equipment models;
- advanced dive scenarios;
- uncertainty and sensitivity analysis;
- physiological models where scientifically appropriate;
- richer control strategies;
- parameter estimation;
- optimization;
- data-driven models;
- integration with real or synthetic dive-computer data;
- instructor materials;
- deployment improvements.

# 5. Milestones

| Milestone | Outcome |
|---|---|
| M0 | Repository and architecture established |
| M1 | Physics foundations complete |
| M2 | Gas and buoyancy models complete |
| M3 | Dynamic diver model complete |
| M4 | End-to-end dive simulation complete |
| M5 | Feedback-control labs complete |
| M6 | Quarto book fully integrated |
| M7 | DiveLab V1 released |

# 6. Success Criterion

DiveLab V1 is successful when a learner can begin with basic diving physics and progressively reach a computational understanding of a diver as a dynamic feedback-controlled system, using executable Python experiments throughout the journey.
