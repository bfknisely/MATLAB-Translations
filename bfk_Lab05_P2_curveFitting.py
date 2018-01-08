"""
Created on Tue Dec 12 20:28:55 2017

@author: Brian

Curve fitting
ME 311 Lab 05, Problem 2

The purpose of this code is to create a second-order polynomial fit to given 
data.
"""

import matplotlib.pyplot as plt
import numpy as np
import statistics as stat

plt.close("all")  # close all open figures

xData = [12.5, 25,37.5,50,62.5,75] # x data
yData = [20,59,118,197,299,420] # y data

degree = 2  # Choose order of best-fit polynomial

#%% Compute best fit line and determine R^2 value

fit = np.polyfit(xData, yData, degree)
y6 = np.polyval(fit, xData)  # Calculate y_fit for each x data point

SSE = sum((yData-y6)**2)  # compute SSE
SST = sum((np.array(yData)-stat.mean(yData))**2)  # compute SST
rsq = 1-SSE/SST  # compute R-squared value
rsqStr = "R^2 = {0:0.6f}".format(rsq)

#%% Format string 

eqStr = ""
for n in range(len(fit)):
    if n >= 2:
        s = "{0:0.4f}x^{1:0.0f} + ".format(fit[n],n)
    elif n == 1:
        s = "{0:0.4f}x + ".format(fit[n])
    else:
        s = "{0:0.4f}".format(fit[n])
    eqStr = s + eqStr

#%%
    
x = np.linspace(min(xData), max(xData),num=50)
y = np.polyval(fit, x) 
# Calculate y_fit for finer detail of x (50 points)

fig, ax = plt.subplots()
plt.plot(xData, yData, '*k')
plt.plot(x, y, '-r')
#plt.text(min(xData),max(yData)-10,eqStr)
#plt.text(min(xData),max(yData)-40,rsqStr)
plt.xlabel("Velocity [mph]")
plt.ylabel("Stopping Distance [ft]")
plt.legend(["daters",eqStr])
plt.show()

