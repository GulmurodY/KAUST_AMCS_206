import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.patches import Patch


def getDesignMatrix(x):
    return np.column_stack([np.ones(x.shape[0]), x])

def solver(A, z):
    Q, R = np.linalg.qr(A, mode='reduced')
    c = np.linalg.solve(R, Q.T @ z)

    z_hat = A @ c
    RMS = np.linalg.norm(z - z_hat) / np.sqrt(A.shape[0])
    return RMS, c

# generate random data
a = np.array([0.8, 1.2])
b = 0.5

N = 100
x = 2 * np.random.rand(N, 2) - 1          # x is Nx2
z = x @ a + b + 0.15 * np.random.randn(N)  # add gaussian noise

A = getDesignMatrix(x)
RMS, c = solver(A, z)

print(f"""a1 = {c[1]:.6f} 
a2 = {c[2]:.6f} 
b  = {c[0]:.6f} 
RMS = {RMS:.6f}""")

x1_grid = np.linspace(x[:, 0].min(), x[:, 0].max(), 100)
x2_grid = np.linspace(x[:, 1].min(), x[:, 1].max(), 100)
X1, X2 = np.meshgrid(x1_grid, x2_grid)

# Compute the plane using LSE coefficients: z = c0 + c1*x1 + c2*x2
Z = c[0] + c[1] * X1 + c[2] * X2


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x[:, 0], x[:, 1], z, color='blue', label='Data Points', alpha=0.6)
surf = ax.plot_surface(X1, X2, Z, color='orange', alpha=0.3, edgecolor='none')

ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Z')
plt.title(f"3D Plane Fit\nRMS Error: {RMS}")
ax.legend(handles=[
    plt.Line2D([0], [0], marker='o', color='blue', linestyle='', label='Data Points'),
    Patch(facecolor='orange', alpha=0.3, label='LSE Plane Fit')
])
plot_dir = os.path.join(os.path.dirname(__file__), 'plots')
plot_path = os.path.join(plot_dir, f'prob39.png')
plt.savefig(plot_path, dpi=200, bbox_inches='tight')
plt.show()

"""
output:
a1 = 0.804036 
a2 = 1.189142 
b  = 0.503684 
RMS = 0.148527
"""