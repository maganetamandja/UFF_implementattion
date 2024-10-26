import numpy as np
from scipy import optimize

def f(x):
    """
    Original function we want to minimize.
    x is an array of parameters [a, b, c]
    """
    a, b, c = x
    return a**2 + 3*(b + c) + 0.1 - c

def objective(x):
    """
    Modified objective function that ensures we minimize to zero
    by taking the absolute value
    """
    return abs(f(x))

# Initial guess for parameters [a, b, c]
x0 = [0, 0, 0]

# Use minimize function with different methods
# Method 1: Nelder-Mead (doesn't require derivatives)
result_nm = optimize.minimize(objective, x0, method='Nelder-Mead')

# Method 2: BFGS (uses gradient approximation)
result_bfgs = optimize.minimize(objective, x0, method='BFGS')

# Print results
def print_optimization_result(result, method_name):
    print(f"\n{method_name} Method Results:")
    print(f"Success: {result.success}")
    print(f"Found minimum: {result.fun}")
    print(f"Parameters [a, b, c]: {result.x}")
    print(f"Original function value at minimum: {f(result.x)}")

# Test both methods
print_optimization_result(result_nm, "Nelder-Mead")
print_optimization_result(result_bfgs, "BFGS") 
    
