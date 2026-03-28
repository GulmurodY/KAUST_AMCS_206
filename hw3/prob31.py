#Explanation of the graph:

# The Gauss-Seidel method converges faster than the Jacobi method.
# The Gauss-Seidel method uses updated values within the same iteration,
# which leads to faster convergence compared to the Jacobi method that
# uses only values from the previous iteration.


import numpy as np
import os
import matplotlib.pyplot as plt

n = 100
h = 1 / n

def b(x: float) -> float:
    return x**2 * (1 - x)

def A(n: int) -> np.ndarray:
    A = np.zeros((n - 1, n - 1))
    for i in range(n - 1):
        A[i][i] = 2
        if i > 0:
            A[i][i - 1] = -1
        if i < n - 2:
            A[i][i + 1] = -1
    return A

def D(A: np.ndarray) -> np.ndarray:
    D = np.zeros_like(A)
    for i in range(len(A)):
        D[i][i] = A[i][i]
    return D


def jacobi_iterations(A: np.ndarray, b: np.ndarray, x0: np.ndarray, tol: float = 1e-6, max_iter: int = 1000) -> tuple[np.ndarray, list[float]]:
    D_inv = np.linalg.inv(D(A))
    x = x0.copy()
    residuals = []
    for k in range(max_iter):
        r_k = b - A @ x
        x_new = x + D_inv @ r_k
        residuals.append(np.linalg.norm(b - A @ x_new, ord=np.inf))
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x_new, residuals

def gauss_seidel_iterations(A: np.ndarray, b: np.ndarray, x0: np.ndarray, tol: float = 1e-6, max_iter: int = 1000) -> tuple[np.ndarray, list[float]]:
    x = x0.copy()
    residuals = []
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(len(A)):
            sum1 = np.dot(A[i][:i], x_new[:i])
            sum2 = np.dot(A[i][i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        residuals.append(np.linalg.norm(b - A @ x_new, ord=np.inf))
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            break
        x = x_new
    return x_new, residuals

A_matrix = A(n)
b_vector = np.array([h**2 * b(i * h) for i in range(1, n)])
x0 = np.zeros(n - 1)

jacobi_x, jacobi_residuals = jacobi_iterations(A_matrix, b_vector, x0, max_iter=20000)
gauss_seidel_x, gs_residuals = gauss_seidel_iterations(A_matrix, b_vector, x0, max_iter=20000)

plt.figure(figsize=(10, 6))
plt.semilogy(jacobi_residuals, label='Jacobi', markevery=100)
plt.semilogy(gs_residuals, label='Gauss-Seidel', markevery=100)
plt.xlabel('Iteration Number')
plt.ylabel('Residual (log scale)')
plt.grid(True)
plt.legend()
plot_dir = os.path.join(os.path.dirname(__file__), 'plots')
plot_path = os.path.join(plot_dir, 'prob31.png')
plt.savefig(plot_path, dpi=200, bbox_inches='tight')
plt.show()
plt.close()