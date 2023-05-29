# Import modules
import numpy as np
import matplotlib.pyplot as plt
import netCDF4

## Open the .nc file and assign it to the file object 'f' 
#  mode = 'r' opens as read-only
filename = 'start08_rf01_AWAS_merged_final_v03.nc'
f = netCDF4.Dataset(filename,mode='r')
for v in f.variables:
	print(v)
## Extract variables from the file object
#  The variable name given by the .nc file is in single quotes
#     To identify what variables exist in a .nc file you can use 
#     "ncdump -h filename.nc | more" in linux OR
#     If the file is in netCDF4 format you can use "print(f)" in Python as well
#  The second set of brackets define what indices to read, [:] takes everything 
time = f.variables['UTMID'][:]
lon = f.variables['LONC'][:]
lat = f.variables['LATC'][:]
alt = f.variables['GGALT'][:]
ozone = f.variables['O3_NOAA'][:]

f.close()

## Plotting the data
fig1 = plt.figure(figsize=[9,12])

#Set plot Grid
ax1 = plt.subplot2grid((8,1), (0,0), rowspan=2)

ax2 = plt.subplot2grid((8,1), (3,0))
plt.setp(ax2.get_xticklabels(), visible=False)

ax3 = plt.subplot2grid((8,1), (4,0))
plt.setp(ax3.get_xticklabels(), visible=False)

#ax4 = plt.subplot2grid((8,1), (5,0))
#plt.setp(ax4.get_xticklabels(), visible=False)

#ax5 = plt.subplot2grid((8,1), (6,0))
#plt.setp(ax5.get_xticklabels(), visible=False)

#ax6 = plt.subplot2grid((8,1), (7,0))

# Plotting data
ax1.plot(lon, lat) ## Lat vs Long
ax2.plot(time, alt,c='k') ## Time vs Altitude
ax3.plot(time, ozone,c='r')  ## Time vs Ozone Conc
#ax4.plot()
#ax5.plot()
#ax6.plot()

#plt.tight_layout()
ax1.set_title('Flight Path, Apr. 18, 2008')
ax2.set_title('Observations Collected During Flight')
ax1.set_ylabel('Latitude')
ax2.set_ylabel('Altitude (m)')
ax3.set_ylabel('Ozone (PPB)')
#ax4.set_ylabel('')
#ax5.set_ylabel('')
#ax6.set_ylabel('')

plt.show()
