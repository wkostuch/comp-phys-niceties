''' 
Solve coupled differential equations for radiactive decay
'''

import numpy as np
import matplotlib.pyplot as plt

# N for variable names denotes the number of nuclei

# Define the functions that give the slopes (rates of change)
def R1(N1: float) -> float:
    '''First decay for the parent'''
    global k1
    return -k1*N1

def R2(N1, N2) -> float:
    '''Second decay function for the daughter'''
    global k1
    global k2
    return k1*N1 - k2*N2

# Assign decay constants
k1 = 0.15
k2 = 0.2

# Make arrays with length of how many times we want to check things
num_time = 200
N1 = np.zeros(num_time)
N2 = np.zeros(num_time)

# Set the inital values in the arrays
N1[0] = 1000 # Number of original parent nuclei
# No time has passed, so there are no daughter nuclei caused from the decay
N2[0] = 0 

# Now create an array for the time values
t = np.linspace(0, 30, num_time) 
dt = t[1] - t[0] # Time interval between each calculation

# Use Heun's method to solve this set of equations
for i in range(1, num_time):
    # Use Euler's method to find N1 at the end of the dt interval
    N1_end = N1[i-1] + R1(N1[i-1])*dt 
    # Now pull out Heun's step to improve the approximation
    N1[i] = N1[i-1] + (R1(N1[i-1]) + R1(N1_end))*dt/2

    # Repeat the above for the N2 (daughter) array
    # Euler's approximation for the end of the interval
    N2_end = N2[i-1] + R2(N1[i-1], N2[i-1])*dt
    # Heun's correction again
    N2[i] = N2[i-1] + (R2(N1[i-1], N2[i-1]) + R2(N1_end, N2_end)) * dt/2

# Now plot the values from Heun's method
# Normal plots
plt.plot(t, N1, 'r-', label= 'Parent')
plt.plot(t, N2, 'b-', label= 'Daughter')
# Semi-log scale plots
#plt.semilogy(t, N1, 'r-', label='Parent') 
#plt.semilogy(t, N2, 'b-', label='Daugheter')
plt.xlabel("Time")
plt.ylabel("Number of Nuclei")
plt.title("Radioactive Decay")
plt.legend()
plt.tight_layout()
plt.show()
