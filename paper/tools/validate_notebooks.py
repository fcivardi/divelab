from __future__ import annotations

import json
import os
import shutil
import time
from pathlib import Path

import nbformat


ROOT = Path(__file__).resolve().parents[2]
OUT = Path("/tmp/divelab-executed")
OUT.mkdir(parents=True, exist_ok=True)
PAPER_FIGURES = ROOT / "paper" / "generated"
PAPER_FIGURES.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", "/tmp/divelab-mpl")

SELECTED_FIGURES = {
    ("02_Boyles_Law.ipynb", 1): "boyle-volume-depth.png",
    ("06_Equilibria_and_Stability.ipynb", 4): "saddle-vector-field.png",
    ("07_Observability_and_State_Estimation.ipynb", 3): "differentiation-noise.png",
    ("07_Observability_and_State_Estimation.ipynb", 4): "observer-estimate.png",
    ("10_Feedback_Control.ipynb", 1): "open-closed-loop.png",
    ("11_PID_Control.ipynb", 2): "anti-windup.png",
    ("18_Integrated_DiveLab_Capstone.ipynb", 6): "capstone.png",
}

results = []
for source in sorted((ROOT / "notebooks").glob("*.ipynb")):
    started = time.monotonic()
    record = {"notebook": source.name, "status": "passed"}
    try:
        nb = nbformat.read(source, as_version=4)
        figure_dir = OUT / "figures" / source.stem
        figure_dir.mkdir(parents=True, exist_ok=True)
        namespace = {"__name__": "__main__"}
        figure_count = 0
        for cell_number, cell in enumerate(nb.cells, start=1):
            if cell.cell_type != "code" or not cell.source.strip():
                continue
            exec(
                compile(cell.source, f"{source.name}:cell-{cell_number}", "exec"),
                namespace,
            )
            import matplotlib.pyplot as plt

            for number in plt.get_fignums():
                figure_count += 1
                output_figure = figure_dir / f"figure-{figure_count:02d}.png"
                plt.figure(number).savefig(
                    output_figure,
                    dpi=180,
                    bbox_inches="tight",
                )
                selected_name = SELECTED_FIGURES.get((source.name, figure_count))
                if selected_name:
                    shutil.copy2(output_figure, PAPER_FIGURES / selected_name)
            plt.close("all")
        record.update(figures=figure_count, errors=0)
    except Exception as exc:
        record.update(status="failed", error=f"{type(exc).__name__}: {exc}")
    record["seconds"] = round(time.monotonic() - started, 2)
    results.append(record)
    print(json.dumps(record), flush=True)

(OUT / "validation.json").write_text(json.dumps(results, indent=2) + "\n")
raise SystemExit(1 if any(r["status"] == "failed" for r in results) else 0)
