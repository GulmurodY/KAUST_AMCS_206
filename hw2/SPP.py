import numpy as np

def chop(x, t=3):
    if x == 0: 
        return 0.0
    
    n = int(np.floor(np.log10(abs(x))))
    mantissa = x / (10**n)
    
    shift = 10**(t - 1)
    chopped_mantissa = np.trunc(mantissa * shift) / shift
    
    return float(chopped_mantissa * (10**n))

def SPP_solver(A, b, t=3):
    n = len(b)
    
    A_b = np.zeros((n, n + 1))
    for i in range(n):
        for j in range(n):
            A_b[i, j] = chop(A[i, j], t)
        A_b[i, n] = chop(b[i], t)
    
    scale = np.array([max(abs(val) for val in row[:-1]) for row in A_b])

    for col in range(n - 1):
        max_ratio = -1.0
        pivot_row = col
        for i in range(col, n):
            ratio = chop(abs(A_b[i, col]) / scale[i], t)
            if ratio > max_ratio:
                max_ratio = ratio
                pivot_row = i
        
        if pivot_row != col:
            A_b[[col, pivot_row]] = A_b[[pivot_row, col]]
            scale[[col, pivot_row]] = scale[[pivot_row, col]]

        for i in range(col + 1, n):
            m = chop(A_b[i, col] / A_b[col, col], t)
            for j in range(col, n + 1):
                product = chop(m * A_b[col, j], t)
                A_b[i, j] = chop(A_b[i, j] - product, t)

    # Back Substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ax = 0.0
        for j in range(i + 1, n):
            product = chop(A_b[i, j] * x[j], t)
            sum_ax = chop(sum_ax + product, t)
        
        numerator = chop(A_b[i, n] - sum_ax, t)
        x[i] = chop(numerator / A_b[i, i], t)
        
    return x

A = np.array([[ 3.03, -12.1, 14.0],
              [-3.03,  12.1, -7.0],
              [ 6.11, -14.2, 21.0]], dtype=float)

b = np.array([-119.0, 120.0, -139.0], dtype=float)

sol = SPP_solver(A, b, t=3)
x_exact = np.linalg.solve(A, b)

print(f"Chopped Solution (3-digit): {sol}")
print(f"Exact Solution (Standard):  {x_exact}")

abs_error = np.linalg.norm(sol - x_exact, np.inf)
rel_error = abs_error / np.linalg.norm(x_exact, np.inf)

print(f"Absolute Error (Infinity Norm): {abs_error:.4f}")
print(f"Relative Error (Infinity Norm): {rel_error:.4f}")