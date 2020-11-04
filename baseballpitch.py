# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:39:35 2020
""
baseballpitch.py
model a pitched baseball trajectory
@author: olenick
"""
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#define the drag coefficient function
def k_D(v):
    delta = 5.0
    vd = 35.0
    return 0.0039 + 0.0058/(1 + np.exp((v-vd)/delta))

#define euler algorithm
def euler(vx,vy,vz, phi):
    #initial conditions
    x = 0
    y = 0
    z = 1.8  #release height in meters
    t = 0
    h = 0.0001  #time step
    k_L = 4.0E-4
    #omega = 1800.0/60.0*2*pi
    g = 9.81
    global X,Y,Z
    X = np.zeros(0)
    Y = np.zeros(0)
    Z = np.zeros(0)

    
    while x <= 18.44:  #distance to home base from pitcher's mound
        X = np.append(X, x)
        Y = np.append(Y, y)
        Z = np.append(Z, z)
        
        v = np.sqrt(vx**2 + vy**2 + vz**2)
        #calculate acceleration components
        ax = -k_D(v)*v*vx + k_L*(vz*omega*np.sin(phi) - vy*omega*np.cos(phi))
        ay = -k_D(v)*v*vy + k_L*(vx*omega*np.cos(phi))
        az = -k_D(v)*v*vz - k_L*vx*omega*np.sin(phi) - g
        
        #apply Euler algorithm
        vx = vx + ax*h
        vy = vy + ay*h
        vz = vz + az*h
        x = x + vx*h
        y = y + vy*h
        z = z + vz*h
        t = t + h
        
TYPE = str(input("Type of pitch:  Fastball(f), Curveball(c), Slider(s), Screwball (sc), No Spin (n) "))
if TYPE == 'c' or TYPE == 'C':
    v = 42.0
    phi = 45.0*np.pi/180.0
    omega = 1800.0/60.0*2*np.pi
if TYPE == 's' or TYPE == 'S':
    v = 42.0
    phi = 0.0
    omega = 1800.0/60.0*2*np.pi
if TYPE =='f' or TYPE == 'F':
    v = 42.0
    phi = 225.0*np.pi/180
    omega = 1800.0/60.0*2*np.pi
if TYPE =='sc' or TYPE == 'SC':
    v = 42.0
    phi = 135*np.pi/180
    omega = 1800.0/60.0*2*np.pi
if TYPE == 'n' or TYPE == 'N':
    v = 42.0
    omega = 0
    phi = 0
   
theta = 1.0*np.pi/180.0  # angle from horizontal

vx = v*np.cos(theta)
vy = 0 #v*sin(theta)
vz = v*np.sin(theta)

euler(vx,vy,vz, phi)

fig = plt.figure()
ax = Axes3D(fig)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.plot(X,Y, zs = Z, zdir = 'z')
plt.show()


    
    
    

       
        
        
        
        
    
    
    
    
    
    
        