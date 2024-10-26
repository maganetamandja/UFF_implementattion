import numpy as np

import matplotlib.pyplot as plt

from scipy import optimize

def f(x):

    return (x**3 - 1)  # only one real root at x = 1

root = optimize.newton(f, 1.5)
print(root)