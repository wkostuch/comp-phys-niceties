# Runge-Kutta example via an autocatalator
# Solves coupled chemical reactions

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


def acc(x: float, v: float, t: float) -> float:
    """Acceleration (second derivative) function.
    x-position, velocity, and time"""
    return -0.5*v - np.sin(x) + 1.15*np.cos(2.0*t/3)
    #return -0.05*v - 2*x 

def xprime(x, y, t) -> float:
    """Differential equation"""
    return np.exp(-0.002*t) - 0.08*x - x*y**2

def yprime(x, y, t) -> float:
    """Another differential equation"""
    return 0.08*x - y + x*y**2

# Set initial values
x = 0
y = 0
tc = np.linspace(0, 1000, 10000) # 1,000 time values
h = 0.1
xc = []
yc = []

# Implement fourth-order Runge-Kutta, or RK4
for t in tc:
    k1y = yprime(x, y, t) * h 
    k1x = xprime(x, y, t) * h
    
    k2y = yprime(x+k1x/2, y + k1y/2, t+h/2) * h 
    k2x = xprime(x+k1x/2, y + k1y/2, t+h/2) * h 

    k3y = yprime(x + k2x/2, y + k2y/2, t + h/2) * h
    k3x = xprime(x + k2x/2, y + k2y/2, t + h/2) * h

    k4y = yprime(x + k3x, y + k3y, + t + h) * h 
    k4x = xprime(x + k3x, y + k3y, + t + h) * h 

    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    y = y + (k1y + 2*k2y + 2*k3y + k4y)/6

    xc.append(x)
    yc.append(y)

# Plot in 3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(tc, xc, zs=yc, zdir='z') # Plot x and v versus t
ax.set_xlim3d(0, 1000)
ax.set_ylim3d(0, 2.5)
ax.set_zlim3d(0, 2.5)


plt.plot(tc, xc, 'r', label="x vs. t")
plt.plot(xc, yc, 'g', label='x vs. y')
plt.legend()
#plt.tight_layout()
plt.show()
