#### HDF Code
# Import modules
import numpy as np
import matplotlib.pyplot as plt
import h5py
from mpl_toolkits.basemap import Basemap

## Open the .he5 file and assign it to the file object 'f' 
#  mode = 'r' opens as read-only
filename = 'OMI-Aura_L3-OMTO3d_2016m0331_v003.he5'
f = h5py.File(filename,mode='r')

## Extract variables from the file object
##lon = f['HDFEOS/GRIDS/OMI Column Amount O3/lon'][:]
##lat = f['HDFEOS/GRIDS/OMI Column Amount O3/lat'][:]
lon =   np.arange(-180.,180.,1)
lat =   np.arange(-90.,90.,1)## Generate Lat since not included in file
ozone = f['HDFEOS/GRIDS/OMI Column Amount O3/Data Fields/ColumnAmountO3'][:,:]
ozone = np.ma.masked_where(ozone==-1.2676506E30, ozone) ## Missing value in metadata
f.close()

## Plotting the data
## turn 1D Lat and Long into 2D
lon2d,lat2d = np.meshgrid(lon,lat)
## Generate filed contours
cf = plt.contourf(lon,lat,ozone,8)
## Generate countour lines
cnt = plt.contour(lon,lat,ozone,8, colors="black")

cb = plt.colorbar(cf)
cb.set_label('O3 in Dobson Units')

plt.title('OMI Column Ozone')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.show()
