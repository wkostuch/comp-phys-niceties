# Cyclist with drag force going on

import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
C_D = 1 # Drag coefficient
rho = 1.225 # Density of air
A = 0.33 # Area of cyclist
v = 4.0 # Initial velocity 
P = 400 # Power output of cyclist
m = 70.0 # Mass of cyclist
g = 9.81
theta = 6

def a(v: float, x: float) -> float:
    """Acceleration function.
    x for hills"""
    # Going uphill for the first km
    if x <= 1000: 
        return -0.5*C_D*rho*A*v*v/m + P/(m*v) - g*np.sin(theta*np.pi/180)
    # Now on flat ground for second km
    elif 1000 <= x <= 2000:
        return -0.5*C_D*rho*A*v*v/m + P/(m*v)
    # Now going downhill on third km
    elif 2000 < x <= 3000:
        return -0.5*C_D*rho*A*v*v/m + P/(m*v) + g*np.sin(theta*np.pi/180)

# Create some arrays 
x_c = np.zeros(0) # x calculated
t_c = np.zeros(0) # time calculated
v_c = np.zeros(0) # Velocity caclulated

# Initial positions
x = 0
t = 0
dt = 0.1

# Now loop around and calculate
while x < 3000:
    # Use Euler's method for this
    # Update velocity, x position, and time
    v = v + a(v, x)*dt
    x = x + v*dt
    t += dt
    # Update arrays
    x_c = np.append(x_c, x)
    v_c = np.append(v_c, v)
    t_c = np.append(t_c, t)


plt.plot(x_c, v_c)
plt.xlabel("x position")
plt.ylabel("velocity")
plt.tight_layout()
plt.show()
