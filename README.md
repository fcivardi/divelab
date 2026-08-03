# DiveLab

> **Teaching Control Engineering Through Scuba Diving**

DiveLab is an open-source executable engineering textbook that uses scuba diving to connect physics, scientific computing, dynamical systems, estimation, feedback control, human decision-making, and integrated-system modeling.

The book explains. The notebooks experiment. Every canonical chapter has a same-numbered Jupyter notebook that runs in Google Colab.

## Learning Path

The manuscript develops one connected causal model:

**depth → pressure → gas volume → buoyancy → motion → state estimation → feedback control → integrated diving systems**

### Part I — Physics of Diving

1. Pressure and Depth
2. Compressible Gases
3. Archimedes' Principle
4. Buoyancy and Vertical Dynamics

### Part II — Dynamical Systems

5. State-Space Models
6. Equilibria and Stability
7. Observability and State Estimation
8. Kalman Filtering

### Part III — Control Engineering

9. Laplace Transforms and Transfer Functions
10. Feedback Control
11. PID Control
12. Frequency Response
13. The Diver in the Loop

### Part IV — Integrated Diving Systems

14. Breathing Dynamics
15. Gas Consumption
16. Dive Computers as Real-Time Estimators
17. Decompression Models
18. The Complete Dive as a Dynamic System

The decompression material explains model states and limitations; it does not generate operational schedules. DiveLab is an engineering text, not a diving qualification, medical assessment, or dive-planning tool.

## Repository Structure

```text
divelab/
├── book/                 # Quarto manuscript, bibliography, and styling
│   ├── part1/            # Chapters 1–4
│   ├── part2/            # Chapters 5–8
│   ├── part3/            # Chapters 9–13
│   ├── part4/            # Chapters 14–18
│   └── appendices/       # Published notebook map and future drafts
├── notebooks/            # Canonical Colab-compatible Notebooks 01–18
├── docs/                 # Editorial, notation, and author guidance
├── ARCHITECTURE.md
├── CURRICULUM.md
├── MANIFESTO.md
├── ROADMAP.md
└── STYLE_GUIDE.md
```

`ARCHITECTURE.md` describes the longer-term engine architecture. Directories proposed there, such as a reusable `src/divelab` package and automated tests, are roadmap items rather than current repository components.

## Read and Run

The active editorial manuscript is maintained on `editorial-v2`. Version 1.0 is frozen.

To preview the book locally:

```bash
git clone https://github.com/fcivardi/divelab.git
cd divelab
git switch editorial-v2
cd book
quarto preview
```

The [Notebook Map](book/appendices/notebook_map.qmd) provides GitHub and Google Colab links for all 18 companion notebooks. The notebooks require no local DiveLab package and use NumPy, SciPy, and Matplotlib.

## Editorial Status

The Chapter 1–18 manuscript and canonical notebook sequence are complete on `editorial-v2`. Current work focuses on whole-book consistency, rendering, references, notebook quality assurance, and release preparation.

## Contributing

Contributions are welcome through issues and focused pull requests. Please read:

- [Style Guide](STYLE_GUIDE.md)
- [Architecture](ARCHITECTURE.md)
- [Roadmap](ROADMAP.md)

Preserve the book-wide notation, chapter–notebook numbering, safety boundaries, and causal progression. Prefer improving existing material over adding parallel explanations.

## Technology

- Quarto
- Jupyter and Google Colab
- Python
- NumPy
- SciPy
- Matplotlib

## License

MIT License.

## Author

**Francesco Civardi**

Data Scientist, Control Engineer, and AI Researcher

## Vision

> Every equation should be executable.
>
> Every model should be reproducible.
>
> Every reader should learn to see the system beneath the phenomenon.
