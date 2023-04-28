# Import modules
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import mpl_toolkits.mplot3d.axes3d as ax3d

## Open the .nc file and assign it to the file object 'f' 
#  mode = 'r' opens as read-only
filename = 'start08_rf01_AWAS_merged_final_v03.nc'
f = netCDF4.Dataset(filename,mode='r')

lon = f.variables['LONC'][:]
lat = f.variables['LATC'][:]
alt = f.variables['GGALT'][:]
ozone = f.variables['O3_NOAA'][:]
f.close()

fig = plt.figure()
ax = ax3d.Axes3D(fig)
ax.plot(lon, lat, alt, marker='o')
ax.set_ylabel('Latitude')
ax.set_xlabel('Longitude')
ax.set_zlabel('Altitude in meters')
ax.view_init(elev=5, azim=-84)
plt.show()














