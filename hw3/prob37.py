import numpy as np
import matplotlib.pyplot as plt

# generate synthetic data for testing the fit
a = [0.5, 1.2]
b = [0.3, 0.8]

x = np.arange(0, 1.01, 0.01)
N = len(x)
w = 2 * np.pi
f = (a[0] * np.cos(w * x) + b[0] * np.sin(w * x) +
     a[1] * np.cos(2 * w * x) + b[1] * np.sin(2 * w * x))
y = f + 0.15 * np.random.randn(N)   # add gaussian noise

plt.plot(x, y, '.')
plt.show()

# your code goes here
