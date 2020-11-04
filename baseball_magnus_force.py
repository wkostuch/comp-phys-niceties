# Baseball example

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define k_D(v) for drag coefficient
def k_D(v):
    """Drag coefficient"""
    delta = 5.0
    vd = 35.0
    return 0.0039 + 0.0058/(1 + np.exp((v-vd)/delta))

def euler(vx, vy, vz, phi):
    """Euler's method"""
    # Initial conditions
    x, y, z = 0, 0, 1.8 # meters
    t = 0
    dt = 0.001
    k_L = 4.00E-4 # Lift coefficient
    g = 9.81 
    global X, Y, Z
    X = np.zeros(0)
    Y = np.zeros(0)
    Z = np.zeros(0)

    # Now loop through for Euler's method
    while x <= 18.44:
        X = np.append(X, x)
        Y = np.append(Y, y)
        Z = np.append(Z, z)
        # Update velocity, then acceleration in each direction
        v = np.sqrt(vx**2 + vy**2 + vz**2)
        ax = -k_D(v)*v*vx + k_L*omega*(vz*np.sin(phi) - vy*np.cos(phi))
        ay = -k_D(v)*v*vy + k_L*omega*vx*np.cos(phi)
        az = -k_D(v)*v*vz - k_L*omega*vx*np.sin(phi) - g
        # Apply Euler
        vx += ax*dt
        vy += ay*dt
        vz += az*dt
        # Update positions
        x += vx*dt
        y += vy*dt
        z += vz*dt
        # Update time
        t += dt


v = 42.0 # meters / second
# Little bit o' spin
theta = 1.0 * np.pi/180 
vx = v*np.cos(theta)
vy = 0
vz = v*np.sin(theta)
#omega = 1800.0 / 60.0 * 2*np.pi
omega = 0
phi = 45 * np.pi/180

euler(vx, vy, vz, phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z label")
ax.plot(X, Y, zs = Z, zdir='z')
plt.show()
