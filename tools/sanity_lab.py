"""Small reproducible checks for course prerequisites and source contracts.

This is not a solution of the six native assignments or a robust-controller test.
"""
from pathlib import Path
import json, re
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.linalg import solve_continuous_lyapunov


def read_matrix(text, name):
    match = re.search(r"^"+name+r"\s*=\s*\[(.*?)\];", text, re.M|re.S)
    if not match:
        raise ValueError("Matrix missing: "+name)
    return np.array([[float(v) for v in re.split(r"[\s,]+", row.strip()) if v]
                     for row in match[1].split(";")])


def run(root):
    k, p = 2., 1.
    h2_time_squared = quad(lambda t:(k*np.exp(-p*t))**2, 0, np.inf)[0]
    h2_freq_squared = quad(lambda w:k*k/(p*p+w*w), 0, np.inf)[0]/np.pi
    assert abs(h2_time_squared-h2_freq_squared)<1e-10
    assert abs(h2_time_squared-k*k/(2*p))<1e-10
    A = np.array([[0., 1.], [-2., -.4]])
    P = solve_continuous_lyapunov(A.T, -np.eye(2))
    residual = A.T@P+P@A+np.eye(2)
    assert np.linalg.eigvalsh(P).min()>0
    assert np.linalg.norm(residual)<1e-10

    def seir(t, x):
        s, e, i, r = x
        u, c1, c2, c3 = .3, 1/60, .2, .1
        infection=u*s*i
        return [-infection+c1*r, infection-c2*e, c2*e-c3*i, c3*i-c1*r]
    sol=solve_ivp(seir,(0,180),[.6,.3,.1,0],rtol=1e-9,atol=1e-11,
                  t_eval=np.linspace(0,180,361))
    assert sol.success
    mass_error=float(np.max(np.abs(sol.y.sum(axis=0)-1)))
    assert mass_error<1e-8
    assert sol.y.min()>-1e-8

    code=(root/"Assignments/f16model.m").read_text(encoding="utf-8-sig")
    matrices={key:read_matrix(code,key) for key in ["A","B","C","D"]}
    expected={"A":(5,5),"B":(5,2),"C":(3,5),"D":(3,2)}
    assert all(matrices[key].shape==expected[key] for key in expected)
    assert matrices["D"][2,1]==.033
    # A p2=0 vertex is not Hurwitz, so no strict common Lyapunov certificate
    # can cover every constant trajectory in the source uncertainty set.
    vertex=np.array([[0.,1.],[-1.,0.]])
    assert np.max(np.abs(np.linalg.eigvals(vertex).real))<1e-12
    result={"status":"passed","h2_time":float(np.sqrt(h2_time_squared)),
        "h2_frequency":float(np.sqrt(h2_freq_squared)),"hinf_scalar_exact":k/p,
        "lyapunov_equation_residual":float(np.linalg.norm(residual)),
        "seir_mass_max_error":mass_error,
        "f16_source_shapes":{key:list(v.shape) for key,v in matrices.items()},
        "f16_direct_term_D32":float(matrices["D"][2,1]),
        "scope":"prerequisite and model-contract checks only; no MATLAB synthesis executed"}
    output=root/"self_study/examples"
    output.mkdir(exist_ok=True)
    (output/"sanity_check.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    (output/"f16_source_matrices.json").write_text(json.dumps(
        {"source":"Assignments/f16model.m","matrices":{k:v.tolist() for k,v in matrices.items()}},
        indent=2),encoding="utf-8")
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result


if __name__=="__main__":
    run(Path(__file__).resolve().parents[2])
