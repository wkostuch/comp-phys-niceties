# Runge-Kutta example via an oscillator; from class

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


def acc(x: float, v: float, t: float) -> float:
    """Acceleration (second derivative) function.
    x-position, velocity, and time"""
    #return -0.5*v - np.sin(x) + 1.5*np.cos(2.0*t/3)
    return -0.05*v - 2*x

# Set initial values
x = -0.75 # Meters
v = 1.2 # Meters per second
tc = np.linspace(0, 100, 1000) # 1,000 time values
h = tc[1] - tc[0]
print(h)
xc = []
vc = []

# Implement fourth-order Runge-Kutta, or RK4
for t in tc:
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
    xc.append(x)
    vc.append(v)

# Plot in 3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(tc, xc, zs=vc, zdir='z') # Plot x and v versus t
ax.set_xlim3d(0, max(tc))
ax.set_ylim3d(min(xc), max(xc))
ax.set_zlim3d(min(vc), max(vc))
plt.show()
