# Lorzens equation mapping in 3-d

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# Define functions
def lorenz(x, y, z, s=10, r=28, b=2.667) -> tuple:
    """Lorenz equation, returns a tuple."""
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return (x_dot, y_dot, z_dot)

dt = 0.01
step_count = 10000
xs = np.empty(step_count+1)
ys = np.empty(step_count+1)
zs = np.empty(step_count+1)

# Set initial values for x, y, and z
xs[0], ys[0], zs[0] = (0, 1, 1.05)

# Generate the curve
for i in range(step_count):
    x_dot, y_dot, z_dot = lorenz(x=xs[i], y=ys[i], z=zs[i])
    xs[i+1] = xs[i] + x_dot * dt
    ys[i+1] = ys[i] + y_dot * dt
    zs[i+1] = zs[i] + z_dot * dt

# Plot it 
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(xs, ys, zs)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
