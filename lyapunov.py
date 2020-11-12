'''
Lyapunov exponent example from class
Measures if a system is chaotic or not.
'''

import numpy as np 
import matplotlib.pyplot as plt 

# Initial values
dx = 0 
sumd = 0 
n = 10000

r = np.linspace(0.01, 1.0, 1000)
lamb = np.zeros(r.size)

'''
Lambda > 0: chaos
Lambda < 0: other type of behavior
'''

# Iteratic the logisistic equation and sum terms to get lambda
for index,i in enumerate(r):
    x = 0.25
    for index2,j in enumerate(np.arange(0, n)):
        dx = 4*i*(1 - 2*x)
        if j > 5000: 
            sumd += np.log(abs(dx))
        x = 4*i*x*(1 - x)
    # Now actually calculate lambda and put it into the array
    lamb[index] = sumd/n/np.log(2)
    sumd = 0

plt.plot(r, lamb, 'r-')
plt.xlabel("r values")
plt.ylabel("Lambda values")
plt.show()
