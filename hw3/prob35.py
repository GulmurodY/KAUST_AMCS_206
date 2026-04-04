import numpy as np
import matplotlib.pyplot as plt
import os

def polynmialDesignMatrix(t, n):
    # create the design matrix for polynomial regression of degree n
    return np.vander(t, N=n + 1, increasing=True)   

def solveProblem3(feature_vector, target_vector, num_data_points, polynomial_degree):
    A = polynmialDesignMatrix(feature_vector, polynomial_degree)
    
    Q, R = np.linalg.qr(A, mode='reduced')
    theta = np.linalg.solve(R, Q.T @ y)

    poly_target = A @ theta  # compute the predicted values using the polynomial model
    RMS = np.linalg.norm(target_vector - poly_target)
    RMS = np.divide(RMS, np.sqrt(num_data_points))

    plt.plot(feature_vector, y, 'o', label="Data points", color="blue")  # plot the points as circles
    plt.plot(feature_vector, poly_target, "--", label='Polynomial fit', color="red")
    plt.legend(loc='upper right')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(f'Degree {polynomial_degree} Polynomial fit to the random dataset \n RMS = {RMS}')
    plot_dir = os.path.join(os.path.dirname(__file__), 'plots')
    plot_path = os.path.join(plot_dir, f'prob35_degree_{polynomial_degree}.png')
    plt.savefig(plot_path, dpi=200, bbox_inches='tight')
    plt.show()
    plt.close()
    return RMS

m = 100   # number of points

# generate random m data points
t = -1 + 2 * np.random.rand(m)
y = t**3 - t + 0.4 / (1 + 25 * t**2) + 0.10 * np.random.randn(m)

# 2. Sort both t and y together using the same indices
sort_idx = np.argsort(t)
t = t[sort_idx]
y = y[sort_idx]

degreeCase = [2, 6, 15]

for degree in degreeCase:
    curRMS = solveProblem3(t, y, m, degree)
    print("polynomial of degree ", degree, "has RMS = ", curRMS)

# I would recommend to use the degree 5 polynomial model(RMS around 0.10296709425131963) since it performs much better than
# the degree 2 polynomial model(RMS around 0.19403384897228942) which underfits the data. Also it is not much worse than the 
# degree 15 polynomail model which most likely to overfit the training data set which will
# result in poor performance in the testing.