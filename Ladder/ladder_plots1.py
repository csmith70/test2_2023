import LHD
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Read in data
file_d = LHD.load_space_data('ozone_fit_regression_components.dat',2)

# Extract variables
year = file_d[:,0]
var1 = file_d[:,1]
var2 = file_d[:,2]
var3 = file_d[:,3]
var4 = file_d[:,4]
var5 = file_d[:,5]
var6 = file_d[:,6]




#========== Plot Setup =================

# Axes position setup parameters
left = 0.1
base = 0.05
base_top = 0.7
del_base = 0.135
width = 0.8
height_upper = 0.25
height_lower = 0.12

# Axis parameters
xmin = 1979
xmax = 2015

# Figure positions
fig = plt.figure(figsize=[9,12])
ax1 = fig.add_axes([left, base_top, width, height_upper])
ax2 = fig.add_axes([left, base+del_base*3, width, height_lower])
ax3 = fig.add_axes([left, base+del_base*2, width, height_lower])
ax4 = fig.add_axes([left, base+del_base, width, height_lower])
ax5 = fig.add_axes([left, base, width, height_lower])
#ax6 = fig.add_axes([left, base+del_base*4, width, height_lower])

# Remove x tick labels
ax1.xaxis.set_ticklabels([])
ax2.xaxis.set_ticklabels([])
ax3.xaxis.set_ticklabels([])
ax4.xaxis.set_ticklabels([])

# Set axis ranges
ax1.set_xlim(xmin, xmax)
ax2.set_xlim(xmin, xmax)
ax3.set_xlim(xmin, xmax)
ax4.set_xlim(xmin, xmax)
ax5.set_xlim(xmin, xmax)

# Plotting data
ax1.plot(year,var1,c='g')
ax1.plot(year,var2,c='k')
ax2.plot(year,var3,c='r')
ax3.plot(year,var4,c=(.6,0,0.6))
ax4.plot(year,var5,c='b')
ax5.plot(year,var6,c=(.6,.6,0))

# Axes Labels and Titles
ax1.set_title('Column Ozone Anomaly (55$^\circ$S to 55$^\circ$N)')
ax2.set_title('Predictor Variables X Regression Coefficients')
ax1.set_ylabel('Column Ozone\nAnomaly (DU)')
ax2.set_ylabel('TSI (DU)')
ax3.set_ylabel('Halogens\n(DU)')
ax4.set_ylabel('Sulfate\nSurface\nArea (DU)')
ax5.set_ylabel('QBO (DU)')



plt.show()


