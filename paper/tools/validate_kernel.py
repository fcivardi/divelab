"""Execute the canonical notebooks in isolated Jupyter kernels and test paper anchors."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

ROOT = Path(__file__).resolve().parents[2]
SELECTED = {
    ("02_Boyles_Law.ipynb", 1): "boyle-volume-depth.png",
    ("06_Equilibria_and_Stability.ipynb", 4): "saddle-vector-field.png",
    ("07_Observability_and_State_Estimation.ipynb", 3): "differentiation-noise.png",
    ("07_Observability_and_State_Estimation.ipynb", 4): "observer-estimate.png",
    ("10_Feedback_Control.ipynb", 1): "open-closed-loop.png",
    ("11_PID_Control.ipynb", 2): "anti-windup.png",
    ("18_Integrated_DiveLab_Capstone.ipynb", 6): "capstone.png",
}
# expression, expected value, absolute tolerance; relative tolerance is zero.
ANCHORS = {
    1: [("rho*g", 10051.81625, 1e-7)],
    6: [("k_b", -0.895866307, 1e-8),
        ("lambda_unstable", 0.10266257, 1e-8),
        ("1/lambda_unstable", 9.74064835, 1e-6),
        ("np.max(np.abs(equilibrium_residual))", 0.0, 1e-10),
        ("abs(k_b-k_b_numerical)", 0.0, 1e-7)],
    7: [("difference_rmse", 1.4356, 5e-5),
        ("observer_rmse", 0.00078, 5e-6),
        ("observability_rank", 2, 0)],
    8: [("rmse[1]", 0.01593, 5e-6)],
    10: [("np.sort(np.linalg.eigvals(Acl))", [-0.9, -0.6], 1e-10),
         ("x_d[0,-1]", -0.1089, 5e-5)],
    11: [("metrics(t,x_w[0],app_w)['IAE [m s]']", 177.46660855, 1e-4),
         ("metrics(t,x_aw[0],app_aw)['IAE [m s]']", 5.17334574, 1e-5)],
    12: [("wn", 0.734846923, 1e-8), ("zeta", 1.020620726, 1e-8),
         ("w_bw", 0.465, 0.001)],
    18: [("np.sort(closed_loop_poles)", [-0.55, -0.35], 1e-10),
         ("depth_error[-1]", -0.306, 5e-4)],
}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "paper/_build/kernel-validation")
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    sources = sorted((ROOT / "notebooks").glob("*.ipynb"))
    if len(sources) != 18:
        raise RuntimeError(f"Expected 18 canonical notebooks, found {len(sources)}")
    records = []
    with tempfile.TemporaryDirectory(prefix="divelab-kernel-") as temporary:
        spec_dir = Path(temporary) / "kernels" / "divelab"
        spec_dir.mkdir(parents=True)
        (spec_dir / "kernel.json").write_text(json.dumps({
            "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
            "display_name": "DiveLab validation", "language": "python"}))
        for source in sources:
            notebook = nbformat.read(source, as_version=4)
            checks = ANCHORS.get(int(source.name[:2]), [])
            figure_dir = output / source.stem
            figure_dir.mkdir(exist_ok=True)
            selected = {str(i): name for (filename, i), name in SELECTED.items() if filename == source.name}
            setup = f'''import os, json, pathlib
os.environ['MPLBACKEND'] = 'Agg'
os.environ['MPLCONFIGDIR'] = {str(output / 'mpl-config')!r}
import matplotlib
matplotlib.use('Agg', force=True)
import matplotlib.pyplot as _dl_plt
_dl_count = 0
_dl_selected = {selected!r}
def _dl_capture():
    global _dl_count
    for _dl_number in _dl_plt.get_fignums():
        _dl_count += 1
        _dl_figure = _dl_plt.figure(_dl_number)
        _dl_path = pathlib.Path({str(figure_dir)!r}) / f'figure-{{_dl_count:02d}}.png'
        _dl_figure.savefig(_dl_path, dpi=180, bbox_inches='tight')
    _dl_plt.close('all')
'''
            original_code = [cell for cell in notebook.cells if cell.cell_type == "code"]
            for cell in original_code:
                if cell.source.strip():
                    cell.source += "\n_dl_capture()"
            audit = f'''import numpy as _dl_np, platform, scipy, nbformat, nbclient, ipykernel
_dl_results = []
for _dl_expr, _dl_expected, _dl_atol in {checks!r}:
    _dl_actual = _dl_np.asarray(eval(_dl_expr), dtype=float)
    assert _dl_np.allclose(_dl_actual, _dl_expected, atol=_dl_atol, rtol=0), (_dl_expr, _dl_actual, _dl_expected)
    _dl_results.append({{'expression': _dl_expr, 'actual': _dl_actual.tolist(), 'expected': _dl_expected, 'atol': _dl_atol}})
pathlib.Path({str(figure_dir / 'audit.json')!r}).write_text(json.dumps({{
    'figures': _dl_count, 'anchors': _dl_results,
    'environment': {{'python': platform.python_version(), 'numpy': _dl_np.__version__, 'scipy': scipy.__version__, 'matplotlib': matplotlib.__version__, 'nbformat': nbformat.__version__, 'nbclient': nbclient.__version__, 'ipykernel': ipykernel.__version__}}
}}, indent=2))
'''
            notebook.cells.insert(0, nbformat.v4.new_code_cell(setup))
            notebook.cells.append(nbformat.v4.new_code_cell(audit))
            manager = KernelManager(kernel_name="divelab", kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(spec_dir.parent)]))
            try:
                NotebookClient(notebook, km=manager, timeout=180, resources={"metadata": {"path": str(ROOT)}}).execute()
                result = json.loads((figure_dir / "audit.json").read_text())
                record = {"notebook": source.name, "status": "passed", **result}
                for index, filename in selected.items():
                    figure = figure_dir / f"figure-{int(index):02d}.png"
                    if not figure.exists():
                        raise RuntimeError(f"Missing selected figure: {filename}")
            except Exception as exc:
                record = {"notebook": source.name, "status": "failed", "error": str(exc)}
            finally:
                if manager.has_kernel:
                    manager.shutdown_kernel(now=True)
            records.append(record)
            print(json.dumps(record), flush=True)
    report = {"execution": "isolated Jupyter kernels with figure capture after each original code cell", "notebooks": records}
    report['passed'] = sum(r['status'] == 'passed' for r in records)
    report['figures'] = sum(r.get('figures', 0) for r in records)
    report['anchors'] = sum(len(r.get('anchors', [])) for r in records)
    report['complete'] = report['passed'] == 18 and report['figures'] == 64
    (output / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != 'notebooks'}))
    return 0 if report['complete'] else 1

if __name__ == "__main__":
    raise SystemExit(main())
