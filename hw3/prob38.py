import numpy as np
import matplotlib.pyplot as plt

# generate random data
N = 100
x = -2 + 4 * np.random.rand(N)
y = (1 + 2 * (x - 1) - 3 * np.maximum(x + 1, 0) +
     4 * np.maximum(x - 1, 0) + 0.2 * np.random.randn(N))

plt.plot(x, y, 'o')
plt.show()

# your code goes here
