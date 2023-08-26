import pygrib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import numpy as np
import numpy.ma as ma
 
plt.figure(figsize=(12,8))
 
grib = 'Odette_091718_750RH_HWRF' # Set the file name of your input GRIB file
grbs = pygrib.open(grib)
print(grbs)

grb = grbs.select()[0]
print(grb)
data = grb.values
data=np.array(data)
print(np.shape(data))
data = ma.masked_values(data, 9999.)
print(np.max(data))
print(np.shape(data))
plt.imshow(data)
plt.show()

# need to shift data grid longitudes from (0..360) to (-180..180)
lons = np.linspace(float(grb['longitudeOfFirstGridPointInDegrees']), \
float(grb['longitudeOfLastGridPointInDegrees']), int(grb['Ni']) )
print(lons)
lats = np.linspace(float(grb['latitudeOfFirstGridPointInDegrees']), \
float(grb['latitudeOfLastGridPointInDegrees']), int(grb['Nj']) )
print(lons.shape)


data, lons = shiftgrid(283., data, lons, start=False)

grid_lon, grid_lat = np.meshgrid(lons, lats) #regularly spaced 2D grid

m = Basemap(projection='cyl', llcrnrlon=-180, \
    urcrnrlon=180.,llcrnrlat=lats.min(),urcrnrlat=lats.max(), \
    resolution='c')

x, y = m(grid_lon, grid_lat)
x2, y2 = m(-72.7, 35.9)

cs = m.pcolormesh(x,y,data[:-1, :-1],shading='flat')
#cs = m.pcolormesh(x,y,data,shading='flat')
m.drawcoastlines()
m.drawmapboundary()
m.drawparallels(np.arange(-90.,120.,30.),labels=[1,0,0,0])
m.drawmeridians(np.arange(-180.,180.,60.),labels=[0,0,0,1])
#plt.clim(0,100)
m.plot(x2,y2,'ro')
plt.colorbar(cs,orientation='vertical', shrink=0.5)
plt.legend()
plt.title('750 mb RH 09.17 18z TS Odette HWRF') # Set the name of the variable to plot
plt.show()



 
