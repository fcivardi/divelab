"""Independent finite-difference, stability and numerical-sensitivity checks."""
import contextlib
import io
import json
import os
from pathlib import Path

os.environ.setdefault('MPLBACKEND', 'Agg')
os.environ.setdefault('MPLCONFIGDIR', '/tmp/divelab-mpl-checks')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
rows = []
for mass in [65., 85., 105.]:
    for density in [1000., 1025.]:
        for depth in [5., 20., 35.]:
            for gas in [0.004, 0.008, 0.012]:
                g, p0 = 9.80665, 101325.
                pressure = p0 + density*g*depth
                fixed = mass/density-gas*p0/pressure
                force = lambda z: density*g*(fixed+gas*p0/(p0+density*g*z))-mass*g
                slope = -(density*g)**2*gas*p0/pressure**2
                fd = (force(depth+0.001)-force(depth-0.001))/0.002
                assert abs(force(depth)) < 1e-10
                assert np.isclose(fd, slope, rtol=1e-7, atol=1e-8)
                A = np.array([[0., -1.], [slope/mass, 0.]])
                poles = np.sort(np.linalg.eigvals(A))
                expected = np.sqrt(-slope/mass)
                assert np.allclose(poles, [-expected,expected], atol=1e-12)
                kp = mass*(0.54-slope/mass); kd = 1.5*mass
                controlled = A-np.array([[0.],[1/mass]])@np.array([[-kp,kd]])
                assert np.allclose(np.sort(np.linalg.eigvals(controlled)), [-0.9,-0.6], atol=1e-12)
                rows.append({'mass':mass,'density':density,'depth':depth,'gas':gas,'slope':slope,'positive_pole':expected})

source = json.loads((ROOT/'notebooks/07_Observability_and_State_Estimation.ipynb').read_text())
observer_rows = []
for dt in [0.005,0.01,0.02]:
    for seed in [7,42,101]:
        namespace = {'__name__':'__main__'}
        with contextlib.redirect_stdout(io.StringIO()):
            for cell in source['cells']:
                if cell['cell_type'] != 'code': continue
                code = ''.join(cell['source']).replace('sample_period = 0.01', f'sample_period = {dt}').replace('np.random.default_rng(42)', f'np.random.default_rng({seed})')
                exec(compile(code,'observer-sensitivity','exec'),namespace)
                plt.close('all')
        assert np.isfinite(namespace['observer_rmse'])
        assert namespace['observer_rmse'] < namespace['difference_rmse']
        observer_rows.append({'dt':dt,'seed':seed,'observer_rmse':float(namespace['observer_rmse']),'difference_rmse':float(namespace['difference_rmse'])})
report = {'parameter_cases':len(rows),'parameter_checks':'neutrality, finite-difference derivative, saddle poles, assigned closed-loop poles','observer_cases':observer_rows,'model_cases':rows}
output = ROOT/'paper/_build/model-checks.json'
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'parameter_cases':len(rows),'observer_cases':len(observer_rows),'status':'passed'}))
