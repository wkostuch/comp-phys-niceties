# Solving a murder with forensics!  
# Or just...solving for body temperature.

import numpy as np
import matplotlib.pyplot as plt

# Parameters from the problem
T_surrounding, r, P = 65, 0.1, 12

# Define the rate function for this example
def R(Temp: float, time: float) -> float:
    return -r*(Temp - T_surrounding*(1+np.cos(2*np.pi*time/P)))

# Create some arrays for time
num_time = 200
t = np.linspace(0, 48, num_time) # Time in hours
dt = t[1] - t[0]

# Create the array for temperature
temperature_array = np.zeros(num_time)
temperature_array[0] = 98.6 # Degrees F

time = 0

# Now apply Heun's algorithm to solve this
for i in range(1, num_time):
    # Set the old time
    old_temp = temperature_array[i-1]

    end_temp = old_temp + R(old_temp, time) * dt
    # Set the end time
    end_time = time + dt

    temperature_array[i] = old_temp + (R(old_temp, time) + R(end_temp, end_time))*dt/2
    time = time + dt

plt.plot(t, temperature_array)
plt.xlabel("Time (hours)")
plt.ylabel("Body Temperature (degrees F)")
plt.show()
