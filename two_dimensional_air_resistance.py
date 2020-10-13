# Dak Prescott
# Aka: air resistance in two dimensions

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import argmax

# Parameters to start off
g = 9.81 # m/s**2
v0 = 20 # m/s, initial velocity
theta = 40 # degrees, initial angle
vt = 9 # m/s, terminal velocity of a pingpong ball

# The variables we'll be using 
t = 0 # seconds
x = 0 # meters
y = 1.25 # meters
dt = 0.01

# Create arrays to store data that is calculated
# They start empty, then we append values as they come
t_calculated = np.zeros(0)
x_calculated = np.zeros(0)
y_calculated = np.zeros(0)


# Define the functions we'll need
def acc_x(v_x: float, v: float) -> float:
    """Acceleration function for x direction."""
    global vt
    return -g*v_x*v/(vt**2)

def acc_y(v_y: float, v: float) -> float:
    """Acceleration function for y direction."""
    global vt
    return -g*(1 + v_y*v/(vt**2))

# Methods of Heun's method
def heun_vel_x(v_x: float, v: float) -> float:
    """Function for Heun's method for velocity in x direction."""
    global dt
    v_x_end = v_x + acc_x(v_x, v)*dt
    v_x = v_x + (acc_x(v_x, v) + acc_x(v_x_end, v))*dt/2
    return v_x

def heun_vel_y(v_y: float, v: float) -> float:
    """Function for Heun's method for velocity in y direction."""
    global dt
    v_y_end = v_y + acc_y(v_y, v)*dt
    v_y = v_y + (acc_y(v_y, v) + acc_y(v_y_end, v))*dt/2
    return v_y

def heun_position(pos: float, vel: float) -> float:
    """Function for the position of the ball, more general function."""
    return pos + vel*dt

# Starting velocity components, with radian conversion
v_x = v0 * np.cos(theta * np.pi/180)
v_y = v0 * np.sin(theta * np.pi/180)
v = v0

# Now let's calculate the velocity and the position as it moves
while y >= 0:
    # Update the velocities and positions, in x and y
    v_x = heun_vel_x(v_x, v)
    x = heun_position(x, v_x)
    v_y = heun_vel_y(v_y, v)
    y = heun_position(y, v_y)
    # Update v
    v = np.sqrt(v_x**2 + v_y**2)
    # Update the arrays
    x_calculated = np.append(x_calculated, x)
    y_calculated = np.append(y_calculated, y)
    # Update the time and time's array
    t = t + dt
    t_calculated = np.append(t_calculated, t)

# Plot the results and figure some things out
plt.xlabel('Horizontal position (m)')
plt.ylabel('Vertical position (m)')
plt.plot(x_calculated, y_calculated, 'r', label='')
plt.title("Ping-pong ball with air resistance")
print(f"Range = {x_calculated[np.argmax(x_calculated)]:0.4f} meters")
# These are two useful lines, argmax gets you the index of the max value in the array
print(f"Max height = {y_calculated[argmax(y_calculated)]:4.2f} meters") 
print(f"Time at max height = {t_calculated[argmax(y_calculated)]:4.2f} seconds")
print(f"Time of flight = {t_calculated[-1]:4.2f} seconds")
plt.show()
