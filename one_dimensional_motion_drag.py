# One-dimensional vertical motion with drag
# Solve Newton's Laws for vertical motion with air resistance

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import argmax

# Parameters to start off
g = 9.81 # m/s**2
v0 = 20 # m/s, initial velocity
vt = 36 # m/s, terminal velocity of a softball

# The variables we'll be using 
t = 0
y = 0
v = v0
dt = 0.01

# Create arrays to store data that is calculated
# They start empty, then we append values as they come
t_calculated = np.zeros(0)
y_calculated = np.zeros(0)


# Define the functions we'll need
def acc(v: float) -> float:
    """Acceleration function."""
    global vt
    return - g*(1 + v*abs(v) / vt**2)

# Methods of Heun's method
def heun_vel(v: float) -> float:
    """Function for Heun's method for velocity."""
    global dt
    v_end = v + acc(v)*dt
    v = v + (acc(v) + acc(v_end))*dt/2
    return v

def heun_y(v: float, y: float) -> float:
    """Function for Heun's method for y position."""
    y_end = y + v*dt # Never actually used...
    y = y + (v + v)*dt/2
    return y


# Now let's calculate the velocity and the position as it moves
while y >= 0:
    # Update velocity and y position; add y to its array
    v = heun_vel(v)
    y = heun_y(v, y)
    y_calculated = np.append(y_calculated, y)
    # Update the time and time's array
    t = t + dt
    t_calculated = np.append(t_calculated, t)

# Plot the results and figure some things out
plt.xlabel('Time (s)')
plt.ylabel('Vertical position (m)')
plt.plot(t_calculated, y_calculated, 'r', label='Vertical position')
# These are two useful lines, argmax gets you the index of the max value in the array
print(f"Max height = {y_calculated[argmax(y_calculated)]:4.2f} meters") 
print(f"Time at max height = {t_calculated[argmax(y_calculated)]:4.2f} seconds")
print(f"Time of flight = {t_calculated[-1]:4.2f} seconds")
plt.show()
