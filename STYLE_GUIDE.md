# DiveLab Style Guide

**Version:** 1.0\
**Scope:** DiveLab notebooks, course documentation, and v2 refactoring

This guide defines conventions so DiveLab remains consistent, readable,
Colab-friendly, and pedagogically coherent.

## 1. Standard notebook structure

Use this progression when appropriate:

1.  Open in Colab badge
2.  `# DiveLab`
3.  `## Notebook NN — Title`
4.  Guiding question
5.  Learning objectives
6.  Conceptual motivation
7.  Physical/mathematical model
8.  Python implementation
9.  Visualization
10. Interpretation
11. Systems/control connection
12. Exercises
13. Challenge
14. Summary
15. Next notebook

The preferred teaching rhythm is:

**intuition → model → simulation → interpretation → exercise**

## 2. Mathematics in Markdown

Use `$ ... $` for inline mathematics.

``` markdown
The state variable $x(t)$ evolves with time.
```

Use `$$ ... $$` for displayed mathematics.

``` markdown
$$
\dot{x}(t) + a x(t) = u(t)
$$
```

Never use square brackets as equation delimiters:

``` markdown
[ \dot{x}(t) + a x(t) = u(t) ]
```

They are ordinary Markdown text and can render incorrectly in
Jupyter/Colab.

For example, write:

``` markdown
Consider the first-order system:

$$
\dot{x}(t) + a x(t) = u(t)
$$

Under zero initial conditions, its Laplace transform is:

$$
sX(s) + aX(s) = U(s)
$$

Therefore:

$$
X(s) = \frac{1}{s+a}U(s)
$$

and:

$$
G(s) = \frac{X(s)}{U(s)} = \frac{1}{s+a}
$$
```

## 3. LaTeX conventions

Prefer explicit, robust notation:

``` latex
\dot{x}
\frac{X(s)}{U(s)}
P_{\text{amb}}
T_{1/2}
```

Use `\boxed{}` only for central results or major conceptual takeaways,
not every equation.

## 4. Core notation

Keep symbols consistent whenever possible:

  Symbol           Meaning
  ---------------- ----------------------------------------------
  \(z\)            depth, positive downward
  \(v\)            vertical velocity; state the sign convention
  \(P\)            pressure
  (P_0)            surface/reference pressure
  (`\rho`{=tex})   fluid density
  \(g\)            gravitational acceleration
  \(V\)            volume
  (F_B)            buoyancy force
  (F_D)            hydrodynamic drag
  \(G\)            remaining gas resource
  \(x\)            state vector
  \(u\)            control input
  \(y\)            output or measured variable

If a notebook uses another convention, state it explicitly.

## 5. Depth and velocity signs

Recommended DiveLab convention:

-   depth (z`\ge0`{=tex}) increases downward;
-   when (v) is upward-positive,

$$
\dot{z}=-v.
$$

If a notebook instead uses (v=`\dot `{=tex}z), then positive velocity
means descent. Never switch conventions silently.

A depth plot may use:

``` python
plt.gca().invert_yaxis()
```

for intuitive visualization, but the plot orientation must not alter the
mathematical convention.

## 6. Units

Show units in variable definitions, numerical results, and plot axes.

Examples:

-   `Depth [m]`
-   `Time [s]`
-   `Pressure [bar]`
-   `Velocity [m/s]`
-   `Gas use [L/min]`

Clearly label approximations and their units.

## 7. Assumptions and educational scope

Separate physical reality from simplified teaching models.

Use wording such as:

> We use the following simplified model to expose the system dynamics.

Models involving decompression, gas reserves, ascent behavior, or
physiology must not be presented as operational dive-planning tools.

## 8. Python cells

A code cell should normally perform one conceptual task.

Prefer:

``` text
define model
simulate
plot
interpret
```

over one long cell that performs everything.

Use descriptive function names such as:

``` python
ambient_pressure_bar()
buoyancy_force()
simulate_profile()
```

Prefer readable educational code over compact code.

## 9. Plots

Every important plot should have:

-   meaningful title;
-   labeled axes;
-   units;
-   legend when multiple curves are present;
-   grid when useful.

Follow an important plot with a Markdown cell explaining what the
student should notice.

For phase portraits, explicitly discuss equilibrium points, trajectory
direction, stable/unstable directions, and saddle points when present.

## 10. Systems terminology

Introduce terminology after physical intuition.

Preferred sequence:

**physical phenomenon → mathematical relation → simulation → systems
interpretation → formal term**

For example:

**small buoyancy error grows → feedback reinforces motion → trajectories
diverge → unstable equilibrium → positive feedback**

## 11. Feedback architecture

Use these terms consistently:

-   **controller:** diver or mathematical control law;
-   **actuator:** lungs, BCD, fins when relevant;
-   **plant:** diver + equipment + surrounding fluid dynamics;
-   **sensor:** physical measurement device;
-   **estimator:** filter, observer, Kalman filter, or model-based
    reconstruction.

## 12. Measurement vocabulary

Distinguish:

-   **measured** --- directly obtained from a sensor;
-   **derived** --- calculated directly from measurements;
-   **estimated** --- reconstructed using measurements and/or a model;
-   **predicted** --- projected into the future using assumptions and a
    model.

Example:

``` text
pressure → measured
depth → derived
vertical velocity → estimated
future gas use → predicted
tissue compartments → hidden model states
```

## 13. Learning objectives and exercises

Use concrete verbs: explain, derive, compute, simulate, compare,
interpret, identify, model.

Exercises should progress from reproduction to exploration:

1.  reproduce a result;
2.  change a parameter;
3.  explain the effect;
4.  modify the model;
5.  combine previous concepts.

Exercise code cells should contain:

``` python
# Your code here
```

Challenges should integrate several concepts and leave meaningful
implementation choices to the student.

## 14. Colab compatibility

Core notebooks should run in Google Colab without local installation.

Prefer standard libraries:

``` python
import numpy as np
import matplotlib.pyplot as plt
```

If another package is necessary, explain why and install it explicitly.

Before release, test:

**Runtime → Run all**

## 15. Open in Colab badge

Use:

``` text
https://colab.research.google.com/github/fcivardi/divelab/blob/editorial-v2/notebooks/NN_Name.ipynb
```

During editorial-v2 development, badge and companion links must target `editorial-v2` so new or revised notebooks are testable. Normalize the links to `main` immediately before merging the branch.

Test the badge after the notebook has been committed to GitHub.

## 16. Filenames

Use:

``` text
01_Pressure.ipynb
02_Archimedes.ipynb
...
21_Decompression_Models.ipynb
```

Rules:

-   two-digit notebook number;
-   underscores;
-   short descriptive names;
-   no spaces.

## 17. Markdown cell size

Prefer focused Markdown cells rather than long essays.

A good rhythm is:

``` text
idea
equation
interpretation
code
plot
interpretation
```

This also makes later Quarto conversion easier.

## 18. Summary and transitions

Every notebook should finish with a concise summary of the main insight
and a clear transition to the next notebook.

Each notebook should answer:

1.  What new idea did the student learn?
2.  Why does that idea make the next notebook necessary?

## 19. Formatting audit checklist

Before releasing or refactoring a notebook:

-   [ ] Colab badge works
-   [ ] title follows convention
-   [ ] learning objectives are present
-   [ ] `$...$` is used for inline math
-   [ ] `$$...$$` is used for display math
-   [ ] no `[ equation ]` pseudo-LaTeX delimiters
-   [ ] no visible Markdown asterisks inside equations
-   [ ] equations render correctly in Colab
-   [ ] notation is consistent
-   [ ] sign conventions are explicit
-   [ ] plot axes include units
-   [ ] important plots have interpretation cells
-   [ ] code cells are focused
-   [ ] simplified models state assumptions
-   [ ] exercises are present where appropriate
-   [ ] summary identifies the main insight
-   [ ] transition to the next notebook is clear
-   [ ] Runtime → Run all succeeds

## 20. v2 refactoring rule

Freeze Core v1 as the prototype.

For v2, apply this guide systematically while preserving the strongest
explanations, simulations, and discoveries from v1.

The objective is:

$$
\boxed{
\text{consistent notation}
+
\text{clear pedagogy}
+
\text{reproducible code}
+
\text{coherent systems narrative}
}
$$

## 21. DiveLab narrative principle

The course should preserve this arc:

$$
\boxed{
\text{Physics}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Estimation}
\rightarrow
\text{Control}
\rightarrow
\text{Integrated Diving Systems}
}
$$

This continuity is the defining style of DiveLab.

## 22. Quarto book heading hierarchy

In a book chapter, the YAML title is the chapter-level heading. Do not add
another level-1 heading inside the same file. In `index.qmd`, keep book-level
title, subtitle, and author metadata in `_quarto.yml`; omit duplicate file-level
YAML title metadata and use an unnumbered level-1 heading for the page.
Mark subsections within unnumbered front matter as `{.unnumbered}` as well.

Use the following hierarchy:

- front matter such as Welcome, Preface, and How to Use This Book:
  level-1 heading with the \`{.unnumbered}\` class;
- chapter title: YAML \`title\` field, rendered as level 1;
- standard chapter sections: level 2 (\`##\`);
- subsections within Theory or Worked Examples: level 3 (\`###\`).

For example:

\`\`\` markdown
---
title: "Pressure and Depth"
---

## Companion Resources

## Engineering Question

## Theory

### Pressure in a Fluid at Rest

## Worked Examples

### Example 1: Absolute Pressure at 18 m
\`\`\`

With numbered sections enabled, this produces chapter numbering such as
\`4\`, \`4.1\`, and \`4.4.1\`, rather than treating every chapter section
as a new chapter.
