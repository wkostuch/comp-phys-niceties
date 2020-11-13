# Poincare oscillater
# Plot the Poincare plot for a damped driven oscillator

import numpy as np 
import matplotlib.pyplot as plt 


def acc(x: float, v: float, t: float) -> float:
    """Acceleration (second derivative) function.
    x-position, velocity, and time"""
    return -k*v - np.sin(x) + c*np.cos(omega*t)

# Set initial values
x = 0 # Meters
v = 0 # Meters per second
k = 0.5 
omega = 2.0/3  #0.005 gives 1 point -> period 1
c = 1.78
n = 1000
i = 1
xs = np.array([])
vs = np.array([])
h = 2*np.pi/omega/n # Units of time

t = 0
# Implement fourth-order Runge-Kutta, or RK4
while t < 1000:
    k1v = acc(x, v, t) * h 
    k1x = v * h 
    
    k2v = acc(x+k1x/2, v + k1v/2, t+h/2) * h 
    k2x = (v + k1v/2) * h 

    k3v = acc(x + k2x/2, v + k2v/2, t + h/2) * h
    k3x = (v + k2v/2) * h 

    k4v = acc(x + k3x, v + k3v, + t + h) * h 
    k4x = (v + k3v) * h

    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    v = v + (k1v + 2*k2v + 2*k3v + k4v)/6
    
    # Keep the values in [-pi, pi] range
    if x > np.pi:
        x = x - 2*np.pi
    if x < -np.pi:
        x = x + 2*np.pi


    # Important step!  "Strobe" effect for collecting points
    # Count of how many times the item has gone around
    value = int(round(omega*t/(2*np.pi)))
    if value == i: 
        # Get rid of initial transcient behavior
        if t > 100:
            xs = np.append(xs, x)
            vs = np.append(vs, v)
        i += 1
    t += h 

plt.plot(xs, vs, 'r.')
plt.title("Poincare map")
plt.xlabel("x position")
plt.ylabel("velocity")
plt.show()
