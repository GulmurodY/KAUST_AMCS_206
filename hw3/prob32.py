import numpy as np
from scipy.linalg import solve, inv, norm
from scipy.sparse.linalg import onenormest

t = np.arange(1, 9.0, 0.5)
n = len(t)

A = np.vander(t, increasing=True)

cond_est = norm(A, 1) * onenormest(inv(A))
print(f"Estimated Condition Number (1-norm): {cond_est:.2e}")

x_true = np.ones(n)
b = A @ x_true

x_computed = solve(A, b)

print("Computed Solution:", x_computed)
residual_norm = norm(A @ x_computed - b) / norm(b)
print(f"Relative Residual Error: {residual_norm:.2e}")

solution_error = norm(x_computed - x_true) / norm(x_true)
print(f"Relative Solution Error: {solution_error:.2e}")

"""
Output of the code when run:

(anm_env) yorovg@Kl-29058 hw3 % python prob32.py
/Users/yorovg/Desktop/AMCS 206/hw3/prob32.py:10: LinAlgWarning:
An ill-conditioned matrix detected: slice 0 has
rcond = 1.1137166192559401e-21.
  cond_est = norm(A, 1) * onenormest(inv(A))
Estimated Condition Number (1-norm): 1.30e+21
/Users/yorovg/Desktop/AMCS 206/hw3/prob32.py:16: LinAlgWarning:
An ill-conditioned matrix detected: slice 0 has
rcond = 1.1137166192559401e-21.
  x_computed = solve(A, b)
Computed Solution:
[ 1.15955387e+03 -5.34499444e+03  1.10115136e+04 -1.34755015e+04
  1.09986942e+04 -6.35529777e+03  2.69561398e+03 -8.54117168e+02
  2.06228024e+02 -3.63195331e+01  6.10860061e+00  4.82225704e-01
  1.03766589e+00  9.98140937e-01  1.00005574e+00  9.99999234e-01]
Relative Residual Error: 1.32e-16
Relative Solution Error: 5.60e+03

Conclusion:
The relative residual error is very small, so the computed solution
satisfies the linear system with high accuracy.
However, the relative solution error is extremely large, which indicates
strong ill-conditioning of matrix A.
The estimated condition number is on the order of 10^21, confirming
that A is ill-conditioned. Small perturbations in input data can lead
to large changes in the computed solution.
"""