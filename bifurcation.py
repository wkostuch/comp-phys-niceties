# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 17:32:03 2020

@author: RPO
"""
import numpy as np
import matplotlib.pyplot as plt
xs = []
rs = []

for r in np.arange(0.9, 0.94, 0.0001):
    x = 0.25
    for i in range(900):
        #x = 4*r*x*(1-x)
        x = 4*r*np.sin(x)
        if (i > 800):
            xs.append(x)
            rs.append(r)
            

plt.plot(rs,xs, 'b.')
plt.show()
