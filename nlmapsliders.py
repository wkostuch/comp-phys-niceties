# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 07:39:09 2020

@author: RPO
"""
import numpy as np
import matplotlib.pyplot as plt  #from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

ax = plt.subplot(111)
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.01)
tcount = len(t)

xs = np.zeros((tcount,))
xs[0] = 0.55
a0 = 0.55
r = 0.25
r0 = 0.25

for i in range(0, tcount-1):
    #xs[i+1] = 4.0*r*xs[i]*(1.0-xs[i])
    xs[i+1] = 4*r*np.sin(xs[i])

l, = plt.plot(t,xs, lw=2, color='red')
plt.axis([0, 1, 0, 1])



axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
axamp  = plt.axes([0.25, 0.15, 0.65, 0.03])

rfreq = Slider(axfreq, 'r', 0.1, 1.0, valinit=r0)
samp = Slider(axamp, 'x0', 0.1, 1.0, valinit=a0)

def update(val):
    amp = samp.val
    r = rfreq.val
    xs[0] = amp
    for i in range(0, tcount-1):
        xs[i+1] = 4.0*r*xs[i]*(1.0-xs[i])
    l.set_ydata(xs)
    plt.draw()
rfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
def reset(event):
    rfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15])
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
def colorfunc(label):
    l.set_color(label)
    plt.draw()
radio.on_clicked(colorfunc)

plt.show()
