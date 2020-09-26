# In-class code for HW4.2, ship firing


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import newton


def fun(theta, yi, yf, v0, xf, xi, v_ship):
    """Function for the Tortuga problem from homework 4, done in class."""
    return (yi - yf + ((v0 * np.sin(theta) * (xf - xi)) / (v0*np.cos(theta) + v_ship)) - \
            (9.8/2) * ((xf - xi)/(v0*np.cos(theta) + v_ship))**2)

# Initial values
# Distance: meters
# Speed: meters per second
xi = 0
yi = 0
xf = 100
yf = 100
v0 = 200
v_ship = (2*1.85e3)/3600

# Now find the root of the equation, which is the firing angle
firing_angle = newton(fun, 25*np.pi/180, args=(yi,yf,v0,xf,xi,v_ship))
print(f"Firing angle: {firing_angle*180/np.pi} degrees")

ship_range = np.linspace(0.514, 1.514, 50)
angles = np.array([newton(fun, 25*np.pi/180, args=(yi,yf,v0,xf,xi,speed)) for speed in ship_range])
plt.plot(ship_range, angles*180/np.pi)
plt.xlabel("Ship speed in meters per second")
plt.ylabel("Firing angle in degrees")
plt.show()