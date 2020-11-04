# Constants
G = 6.67E-11  # Gravitational constant
AU = 1.5E11   # Astronomical unit

from vpython import *

scene = canvas(tittle = "Kepler's First Law", background = color.black)

# Create objects for the sun and earth
sun = sphere(pos=vec(0,0,0), radius = 1E10, mass = 2E30, color=color.yellow)
earth = sphere(pos=vec(AU, 0,0), radius = .8E10, mass=2E24, color=color.blue)

# Initial conditions
earth.vel = vec(0, 1.3*sqrt(G*sun.mass/mag(earth.pos)), 0.1*sqrt(G*sun.mass/mag(earth.pos)))


# Create a trail for the earth
earth.trail = curve(pos=earth.pos, color=earth.color)

# Define a time interval
dt = 1E5 # Time in seconds

# Animation loop
while True:
    r = mag(earth.pos - sun.pos)
    a = -G*sun.mass*(earth.pos-sun.pos) / r**3
    # Update earth's velocity with Euler's method
    earth.vel = earth.vel + a*dt
    earth.pos = earth.pos + earth.vel*dt
    # Give the earth a trail
    earth.trail.append(pos=earth.pos, color=earth.color)
    rate(100) # 100 FPS
