# First order differential equations from class

import numpy as np
import matplotlib.pyplot as plt

# Solve:
#  dy/dy = y**2 + 1    with initial value y(0) = 0

def f(y:float) -> float:
    """The function that we're using for the differential equation: specifies the slope anywhere."""
    return y*y + 1

# Series of x values to use
N = 20
x = np.linspace(0, 1, N)
delta_x = x[1] - x[0]

# Make an array to hold y values
y = np.zeros(N)

# Use Euler's method to populate that y array with initial value of y(0) = 0
for i in range(1, N):
    y[i] = y[i-1] + f(y[i-1])*delta_x
# Plot Euler's
plt.plot(x, y, '.', color='b')

# Plot the analytical solution
plt.plot(x, np.tan(x), '-', color='r')


# Reset the y array for Heun's method
y = np.zeros(N)

# Heun's method for differential equations, a correction on Euler's prediction
for i in range(1, N):
    y_end = y[i-1] + f(y[i-1])*delta_x    # Use Euler's method to make a prediction for the next value: y_n+1 = y_n + f(y_n)*delta_x
    y[i] = y[i-1] + (f(y[i-1]) + f(y_end))*delta_x/2 # Heun's method!  We use Euler's method as a prediction and then correct it and average

# Plot Heun's solution
plt.plot(x, y, '.', color='g')


# Format the plot nicely
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Euler's method", "Analytical solution", "Heun's method"])
plt.tight_layout()
plt.show()
