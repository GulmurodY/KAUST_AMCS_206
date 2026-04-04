"""
The piecewise linear model has smaller RMS(0.17638707987405594) than the linear model RMS(0.6233362922986841). 
Adding the basis functions does not incrase the rms since if the basis functions do not improve the result 
their weights will be zero. Since adding basis functions makes the model more flexible we either get the
same or better results.
"""

import numpy as np
import matplotlib.pyplot as plt
import os


def piecewiseLinearDesignMat(x):
    A = np.zeros((len(x), 4))
    for i, x_i in enumerate(x):
        A[i][0] = 1
        A[i][1] = x_i
        A[i][2] = max(x_i - 1, 0)
        A[i][3] = max(x_i + 1, 0)
     
    return A


def solver(A, x, y):
     Q, R = np.linalg.qr(A, mode='reduced')
     theta = np.linalg.solve(R, Q.T @ y)

     y_hat = A @ theta
     RMS = np.linalg.norm(y - y_hat) / np.sqrt(len(x))
     return RMS, y_hat

# generate random data
N = 100
x = -2 + 4 * np.random.rand(N)
y = (1 + 2 * (x - 1) - 3 * np.maximum(x + 1, 0) +
     4 * np.maximum(x - 1, 0) + 0.2 * np.random.randn(N))

sort_idx = x.argsort()
x = x[sort_idx]
y = y[sort_idx]


A_lin = np.column_stack([np.ones(len(x)), x])
A_plin = piecewiseLinearDesignMat(x)

linRMS, y_hat_lin = solver(A_lin, x, y)
plinRMS, y_hat_plin = solver(A_plin, x, y)

print(f"""RMS for linear model:           {linRMS} 
RMS for piecewise linear model: {plinRMS}""")


plt.plot(x, y_hat_lin,  '--', label="Linear model",           color="blue")
plt.plot(x, y_hat_plin, '--', label="Piecewise Linear model", color="green")
plt.plot(x, y,          'o',  label="Data points",            color='red')
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Linear model(RMS={linRMS}) vs \n Piecewise linear model(RMS={plinRMS})')
plot_dir = os.path.join(os.path.dirname(__file__), 'plots')
plot_path = os.path.join(plot_dir, f'prob38.png')
plt.savefig(plot_path, dpi=200, bbox_inches='tight')
plt.show()

# ouptut:
# RMS for linear model:           0.6233362922986841 
# RMS for piecewise linear model: 0.17638707987405594