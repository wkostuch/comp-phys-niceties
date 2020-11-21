# Rossler equation mapping in 3-d
# This was used back in the day for the realization
# that heart beats could be mapped!  Kind of important...

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# Define functions
def rossler(x, y, z, a=0.398, b=2, c=4) -> tuple:
    """Rossler equation, returns a tuple."""
    x_dot = -y - z
    y_dot = x + a*y
    z_dot = b + z*(x - c)
    return (x_dot, y_dot, z_dot)

dt = 0.01
step_count = 10000
xs = np.empty(step_count+1)
ys = np.empty(step_count+1)
zs = np.empty(step_count+1)
times = np.empty(step_count+1)
times[0] = 0

# Set initial values for x, y, and z
xs[0], ys[0], zs[0] = (0, 1, 1.05)

# Generate the curve
for i in range(step_count):
    x_dot, y_dot, z_dot = rossler(x=xs[i], y=ys[i], z=zs[i])
    xs[i+1] = xs[i] + x_dot * dt
    ys[i+1] = ys[i] + y_dot * dt
    zs[i+1] = zs[i] + z_dot * dt
    times[i+1] = i*dt 

# Plot it 
fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.plot(xs, ys, zs)
ax.set_xlabel('x axis')
ax.set_ylabel('y axiz')
ax.set_zlabel('z axis')
plt.show()

# Y as a function of t 
plt.plot(times, ys)
plt.xlabel("Time")
plt.ylabel("Y value")
plt.title("Y as a function of time")
plt.tight_layout()
plt.show()
