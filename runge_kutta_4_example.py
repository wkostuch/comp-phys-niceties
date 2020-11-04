# Runge-Kutta 4 example

import numpy as np 
import matplotlib.pyplot as plt

'''
Application of the RK4 algorithm
Want to solve dx/dt = 1 - t*sin(x) with initial condition x = 0 at t = 0
Up to t = 10
'''

def der(x: float, t: float) -> float:
    """Derivative function from above."""
    return 1 - t * np.sin(x)

# Initial conditions
t0, x0 = 0, 0
h = 0.01

# Create arrays for storing computed values
tc = np.arange(0, 10, h)
xc = []
x = x0

for index,t in enumerate(tc):
    k1 = der(x, t) * h 
    k2 = der(x + k1/2, t + h/2) * h
    k3 = der(x + k2/2, t + h/2) * h
    k4 = der(x * k3, t + h) * h
    x += (k1 + 2*k2 + 2*k3 + k4) / 6
    xc.append(x)

plt.plot(tc, xc)
plt.xlabel("Time (s)")
plt.ylabel("x(t)")
plt.show()
