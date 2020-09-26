# Root finding code from class

import numpy as np
from scipy.optimize import fsolve, bisect, newton
import matplotlib.pyplot as plt


# Define a function for the function we're dealing with
def func(x):
    return np.exp(-x) - np.cos(x)

# Create an x-axis array of values
x_values = np.linspace(-2, 2, 100)
y_values = func(x_values)

# Plot the curves
plt.plot(x_values, y_values, 'r-')
plt.plot(x_values, np.zeros(100), 'b-')
plt.xlabel("x")
plt.ylabel('exp(-x) - cos(x)')
plt.show()

# Print the solution
print(f"fsolve: {fsolve(func, 1.3)}") #1.3 is the starting point for solving it
print(f"bisect: {bisect(func, 0.1,2)}")
print(f"newton: {newton(func, 1.3)}")