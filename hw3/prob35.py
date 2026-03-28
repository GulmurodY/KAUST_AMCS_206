import numpy as np
import matplotlib.pyplot as plt

m = 100   # number of points

# generate random m data points
t = -1 + 2 * np.random.rand(m)
y = t**3 - t + 0.4 / (1 + 25 * t**2) + 0.10 * np.random.randn(m)

plt.plot(t, y, 'o')  # plot the points as circles
plt.show()
