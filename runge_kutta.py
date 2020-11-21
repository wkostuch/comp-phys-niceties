# Runge-Kutta example via an oscillator; from class

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


def acc(x: float, v: float, t: float) -> float:
    """Acceleration (second derivative) function.
    x-position, velocity, and time"""
    return -0.5*v - np.sin(x) + 1.5*np.cos(1.0*t/3)
    #return -0.05*v - 2*x 

# Set initial values
x = -0.75 # Meters
v = 1.2 # Meters per second
tc = np.linspace(0, 100, 1000) # 1,000 time values
h = 0.1
xc = []
vc = []

# Implement fourth-order Runge-Kutta, or RK4
for t in tc:
    k1v = acc(x, v, t) * h 
    k1x = v * h 
    
    k2v = acc(x+k1x/2, v + k1v/2, t+h/2) * h 
    k2x = (v + k1v/2) * h 

    k3v = acc(x + k2x/2, v + k2v/2, t + h/2) * h
    k3x = (v + k2v/2) * h 

    k4v = acc(x + k3x, v + k3v, + t + h) * h 
    k4x = (v + k3v) * h

    x = x + (k1x + 2*k2x + 2*k3x + k4x)/6
    v = v + (k1v + 2*k2v + 2*k3v + k4v)/6
    
    # Keep values in a confined range
    if x > np.pi:
        x = x - 2*np.pi
    if x < -np.pi:
        x = x + 2*np.pi
    
    xc.append(x)
    vc.append(v)

# Plot in 3D
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(tc, xc, zs=vc, zdir='z') # Plot x and v versus t
ax.set_xlim3d(0, max(tc))
ax.set_ylim3d(min(xc), max(xc))
ax.set_zlim3d(min(vc), max(vc))
plt.show()

# Use a fast Fourier transform (FFT) to calculate the spectrum

spectrum = np.fft.fft(xc) # Produce the FFT
# Now find the frequencies 
frequency = np.fft.fftfreq(spectrum.size, d= h)
index = np.where(frequency >= 0)

# Scale the FFT and clip the data
clipped_spectrum = h * spectrum[index].real
clipped_frequency = frequency[index]

# Create a figure 
fig = plt.figure()
fig.subplots_adjust(hspace=0.5)

# Create xy plot of the amplitude and transform with labeled axes
data1 = fig.add_subplot(2,1,1)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Damped Forced Oscillator")
data1.plot(tc, xc, color='r', label='Amplitude')
plt.legend()
plt.xlim(0, 100)

data2 = fig.add_subplot(2,1,2)
plt.xlabel("Frequency")
plt.ylabel("Signal (Power)")
plt.title("Spectrum of the Damped Forced Oscillator")
data2.plot(clipped_frequency, clipped_spectrum**2, color='b', label='FFT', linewidth=1.5)
plt.legend()
plt.xlim(0, 1)

plt.show()
