"""
Created on Wed Dec 13 17:26:23 2017

@author: Brian

ME311 Lab 11: Fourier

Read data file acc2.dat and plot frequencies

Construct a signal sampled at 500 Hz for 10 seconds with an amplitude of
4 at 4 Hz, 6 at 6 Hz, and 10 at 20 Hz. 
"""

import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

fs = 1000  # Define sampling frequency in Hz
f = open('acc2.dat','r')  # Open file
message = f.read()  # Read file
strlist = message.split('\n')  # Separate file into list based on newline 
datalist = []  # Initialize array
for item in strlist:
    if item:
        datalist.append(float(item))

f.close()  # Close file

datanorm = np.subtract(datalist, stat.mean(datalist))
n = len(datanorm)
time = np.linspace(0, len(datanorm)/fs, len(datanorm))

y = np.fft.fft(datanorm)/n
powerY = np.power(abs(y),2)

k = np.arange(n)
tt = n/fs
frq = k/tt # two sides frequency range
frq = frq[range(int(n/2))] # one side frequency range

plt.subplot(2, 1, 1)  # create time signal plot
plt.plot(time, datalist)
plt.xlabel('Time [s]')
plt.ylabel('Voltage [V]')

plt.subplot(2, 1, 2)  # create frequency plot
plt.plot(frq, abs(y), 'r')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power')