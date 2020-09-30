# First order differential equations from class

import numpy as np
import matplotlib.pyplot as plt

# Solve:
#  dy/dy = y**2 + 1    with initial value y(0) = 0

def f(y:float) -> float:
    """The function that we're using for the differential equation: specifies the slope anywhere."""
    return y*y + 1

# Series of x values to use
N = 100
x = np.linspace(0, 1, N)
delta_x = x[1] - x[0]

# Make an array to hold y values
y = np.zeros(N)

# Use Euler's method to populate that y array with initial value of y(0) = 0
for i in range(1, N):
    y[i] = y[i-1] + f(y[i-1])*delta_x

# Now plot it
plt.plot(x, y, '.', color='b')
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, np.tan(x), '-', color='r')
plt.legend(["Euler's method", "Analytical solution"])
plt.tight_layout()
plt.show()
