"""
The plotted error |f(mid)| is not monotonic: it oscillates up and down because
bisection only guarantees that the bracketing interval halves each step, not
that the midpoint's residual decreases. Still, the overall trend is downward.
"""
import math
import matplotlib.pyplot as plt
import os

def bisectionMethod(a, b, f, tolerance=10 ** -6):
    f_a, f_b = f(a), f(b)

    if f_a * f_b >= 0:
        raise Exception("The function has same sign values in the endpoints")



    iteration = 0
    iter_error = []
    mid = (a + b) / 2
    f_mid = f(mid)
    while abs(a - b) >= tolerance and iteration < 1000:
        iter_error.append(abs(f_mid))
        if f_mid == 0:
            break
        elif f_a * f_mid < 0:
            b = mid
        else:
            a = mid
            f_a = f_mid
            
        iteration += 1
        mid = (a + b) / 2
        f_mid = f(mid)

    iter_error.append(abs(f_mid))

    print(f"root ≈ {mid}, f(root) ≈ {f_mid}, iterations = {iteration - 1}")

    plt.semilogy(range(1, len(iter_error)), iter_error[1:], marker='o')
    plt.xlabel('k')
    plt.ylabel('|f(x)|')
    plt.title('Bisection Method: Function Error vs Iteration(semilog)')

    script_name = os.path.splitext(os.path.basename(__file__))[0]
    plt.savefig(os.path.join(os.path.dirname(__file__), 'plots', f'{script_name}.png'))
    plt.show()



def f(x):
    return x ** 3 - math.sin(x)

a, b = 0.5, 2.0
tolerance = 10 ** -6

bisectionMethod(a, b, f, tolerance)
"""
output:
root ≈ 0.9286266565322876, f(root) ≈ 6.914647059375056e-07, iterations = 20
"""