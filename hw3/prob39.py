import numpy as np
import matplotlib.pyplot as plt

# generate random data
a = np.array([0.8, 1.2])
b = 0.5

N = 100
x = 2 * np.random.rand(N, 2) - 1          # x is Nx2
z = x @ a + b + 0.15 * np.random.randn(N)  # add gaussian noise

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x[:, 0], x[:, 1], z, marker='o')
ax.grid(True)
plt.show()

# your code goes here
