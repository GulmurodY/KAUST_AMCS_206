import numpy as np
import matplotlib.pyplot as plt
import os


def sinusoidDesignMatrix(w_1, w_2, x):
     A = np.zeros((len(x), 4))
     for i, x_i in enumerate(x):
          A[i][0] = np.cos(w_1 * x_i)
          A[i][1] = np.sin(w_1 * x_i)
          A[i][2] = np.cos(w_2 * x_i)
          A[i][3] = np.sin(w_2 * x_i)
     return A


# generate synthetic data for testing the fit
a = [0.5, 1.2]
b = [0.3, 0.8]

x = np.arange(0, 1.01, 0.01)
N = len(x)
w = 2 * np.pi
f = (a[0] * np.cos(w * x) + b[0] * np.sin(w * x) +
     a[1] * np.cos(2 * w * x) + b[1] * np.sin(2 * w * x))
y = f + 0.15 * np.random.randn(N)   # add gaussian noise

A = sinusoidDesignMatrix(w, 2*w, x)
Q, R = np.linalg.qr(A, mode='reduced')
theta = np.linalg.solve(R, Q.T @ y)

y_hat = A @ theta  # compute the predicted values using the trigonometric model
RMS = np.linalg.norm(y - y_hat) / np.sqrt(len(x))

print(f"a1 = {theta[0]:.4f}, b1 = {theta[1]:.4f}")
print(f"a2 = {theta[2]:.4f}, b2 = {theta[3]:.4f}")
print(f"RMS = {RMS:.6f}")

plt.plot(x, y, 'o', label="Data points", color="blue")  # plot the points as circles
plt.plot(x, y_hat, "--", label='Fit', color="red")
plt.legend(loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Sinusoid fit to the dataset \n RMS = {RMS}')
plot_dir = os.path.join(os.path.dirname(__file__), 'plots')
plot_path = os.path.join(plot_dir, f'prob37.png')
plt.savefig(plot_path, dpi=200, bbox_inches='tight')
plt.show()
plt.close()

#Terminal output(the plot is in the plots directory):
# a1 = 0.5310, b1 = 0.3041
# a2 = 1.2004, b2 = 0.7966
# RMS = 0.151989