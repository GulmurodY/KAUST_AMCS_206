import math

#for this problem lets set the default values 
# for the arguments same as the ones in the statment
# we can manually change them later

def f(x: float) -> float:
    return x ** 3 - 2*x - 5

def df_dx(x: float) -> float:
    return 3 * x ** 2 - 2

def Newton(f, df_dx, a=2.0, b=3.0, initial_guess = 2.5, accuracy=10 ** -6, iter_limit=1000):
    cur = initial_guess
    for k in range(iter_limit):
        f_cur = f(cur)
        df_cur = df_dx(cur)
        if df_cur != 0:      
            cur -= f_cur / df_cur
        else:
            raise Exception(f'Derivative is zero at iteration {k}')
        
        if abs(f(cur) < accuracy):
            return cur, k, f(cur)
    


print(*Newton(f, df_dx))




