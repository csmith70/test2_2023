import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Load the 2-D heights data
z = np.load('heights.npy')

# must use np.transpose for many AOSC Data Sets
# matplotlib expects 2D data arrays to be in form of (rows, columns)
# AOSC often orders data (Displacement East, Displacement North)
shape = np.shape(z)
print(shape)

# Need to make an x,y grid to plot the heights(z) on
# The grid is actually a 5km grid not default 1
x = np.arange(0,shape[0])*5
y = np.arange(0, shape[1])*5

# extends adds arrow to end of colorbar: "neither", "both", "min", "max"
colormap = cm.get_cmap('hot') # Examples on Page 161
# Plot the filled contours
cf = plt.contourf(x, y, np.transpose(z), levels=range(5500,5701,25), extend="both", cmap=colormap)
# Plot the Contour Lines
cnt = plt.contour(x, y, np.transpose(z), levels=range(5500,5701,25),colors='black')

cb = plt.colorbar(cf, orientation='horizontal')
cb.set_label('meters')
plt.xlabel('km')
plt.ylabel('km')

# add labels to the lines
plt.clabel(cnt, fmt="%.0f", inline=True)
plt.title('Geopotential Heights')
plt.show()

