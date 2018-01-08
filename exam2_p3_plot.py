"""Plot Velocity Ratio and Momentum Flux Ratio vs Blowing Ratio

This code plots Velocity Ratio and Momentum Flux Ratio versus Blowing Ratio.

Brian Knisely
December 11, 2017
"""

import numpy as np
import matplotlib.pyplot as plt
import os

dr = 1.6  # Density Ratio
br = np.linspace(0.5, 40, num=400)  # Blowing Ratio
vr = br/dr  # Velocity Ratio
i = br**2/dr  # Momentum Flux Ratio

fs = 17  # Define font size for figures
fn = 'Calibri'  # Define font for figures
fig2FileName = 'fig2.png'


# Plot velocity ratio vs blowing ratio - general plot format
fig, ax = plt.subplots(dpi=320)
plt.plot(br, vr, ls='dotted', lw=3)
xlab = 'BR'
ylab = 'VR'

###############################################################################
# Block of code to copy-paste for START paper format
###############################################################################
fs = 17  # Define font size for figures
fn = 'Calibri'  # Define font for figures
figFileName = 'fig1.png'
plt.xlabel(xlab, fontsize=fs, fontname=fn, fontweight='bold')
plt.ylabel(ylab+'     ', fontsize=fs, rotation=0, fontname=fn,
           fontweight='bold')
plt.xticks(fontsize=fs-5, fontname=fn, fontweight='bold')
plt.yticks(fontsize=fs-5, fontname=fn, fontweight='bold')
ax.get_xaxis().set_tick_params(direction='in', bottom='on', top='on')
ax.get_yaxis().set_tick_params(direction='in', left='on', right='on')
plt.savefig(figFileName)  # Save figure as file
plt.close(fig)  # Remove figure from console
os.startfile(figFileName)  # Open figure via external photos program
###############################################################################
# End block of code to copy-paste
###############################################################################

# Plot momentum flux vs blowing ratio
fig, ax = plt.subplots(dpi=320)
plt.plot(br, i, ls='dashed', lw=3)
plt.xlabel('BR', fontsize=fs, fontname=fn, fontweight='bold')
plt.ylabel('I     ', fontsize=fs, rotation=0, fontname=fn, fontweight='bold')
plt.xticks(fontsize=fs-5, fontname=fn, fontweight='bold')
plt.yticks(fontsize=fs-5, fontname=fn, fontweight='bold')
ax.get_xaxis().set_tick_params(direction='in', bottom='on', top='on')
ax.get_yaxis().set_tick_params(direction='in', left='on', right='on')
plt.savefig(fig2FileName)
plt.close(fig)
