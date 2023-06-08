# Import modules
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import mpl_toolkits.mplot3d.axes3d as ax3d

fig = plt.figure()
ax = ax3d.Axes3D(fig)

x, y, z = ax3d.get_test_data(0.05)

## Make Plots
ax.plot_surface(x, y, z, cstride=5, rstride=5, alpha=0.8)
ax.contour(x, y, z, zdir='x', offset=-10)
#ax.contour(x, y, z, zdir='y', offset=40)
#ax.contour(x, y, z, zdir='z', offset=-100)
ax.set_xlabel('X')
ax.set_xlim(-40,40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100,100)

plt.show()
