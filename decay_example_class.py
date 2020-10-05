# First order differential equations from class

import numpy as np
import matplotlib.pyplot as plt

# Solve:
#  dy/dy = y**2 + 1    with initial value y(0) = 0

def R(n:float) -> float:
    """The function that we're using for the differential equation: specifies the slope anywhere."""
    return -k*n

# Series of x values to use
N = 50
t = np.linspace(0, 1, N)
delta_t = t[1] - t[0]

# Decay constant
k = 2.5
#n = 1000 # Original radioactive nuclei

# Make an array to hold y values
n = np.zeros(N)
n[0] = 1000

# Use Euler's method to populate that y array with initial value of y(0) = 0
for i in range(1, N):
    n[i] = n[i-1] + R(n[i-1])*delta_t
# Plot Euler's
plt.plot(t, n, '.', color='b')

# Plot the analytical solution
plt.plot(t, 1000 * np.exp(-k*t), '-', color='r')

# Not necessary, but you can reset the array for Heun's method
n = np.zeros(N)
n[0] = 1000

# Heun's method for differential equations, a correction on Euler's prediction
for i in range(1, N):
    n_end = n[i-1] + R(n[i-1])*delta_t    # Use Euler's method to make a prediction for the next value: y_n+1 = y_n + f(y_n)*delta_x
    n[i] = n[i-1] + (R(n[i-1]) + R(n_end))*delta_t/2 # Heun's method!  We use Euler's method as a prediction and then correct it and average

# Plot Heun's solution
plt.plot(t, n, '.', color='g')

# Format the plot nicely
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(["Euler's method", "Analytical solution", "Heun's method"])
plt.tight_layout()
plt.show()
