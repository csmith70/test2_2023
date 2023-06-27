#Dee Dee's senior research code to produce figures of vertical cross sections of PV in stratospheric intrusions 
#Data from Nasa Global Modeling and Assimilation Office, MERRA-2 reanalysis 

import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.animation import FuncAnimation
#import LHD 
def load_space_data(infile):
	import pandas as pd
	fin = open(infile)
	head = fin.readline().split(',')
	colnames = fin.readline().strip()
	colnames = colnames.split(',')
	ncols = head[0]
	headers = int(head[1])
	fin.close()
	data_in = pd.read_csv(infile, skiprows=headers, delim_whitespace=True, header=None).values
	return data_in,colnames

def load_comma_data(infile):
        import pandas as pd
        fin = open(infile)
        head = fin.readline().split(',')
        colnames = fin.readline().strip()
        colnames = colnames.split(',')
        ncols = head[0]
        headers = int(head[1])
        fin.close()
        data_in = pd.read_csv(infile, skiprows=headers, delim_whitespace=False, header=None).values
        return data_in,colnames


from mpl_toolkits.basemap import Basemap
from mpl_toolkits import mplot3d
import netCDF4
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

filename = 'Melissa_MERRA_1011.nc4'
f = netCDF4.Dataset(filename, mode='r') 
#print(f)
#Extract variables from the file 
#time = f.variables['time'][:]
lat = f.variables['lat'][:]
lon = f.variables['lon'][:]
print(lat[240])
print(lat[257])
EPV = f.variables['EPV'][:]
EPV = np.ma.masked_where(EPV==9.999999870e+14,EPV)
p = f.variables['lev'][:]
Ozone = f.variables['O3'][:]
t = f.variables['time'][:]
print(t[6])
U = f.variables['U'][:]
RH = f.variables['RH'][:]
T = f.variables['T'][:]

f.close()
lat2d, p2d= np.meshgrid(lat,p)
lon2d, p2d=np.meshgrid(lon,p)
print(lon[175])
#print(lon[210])

'''

hour=0
while hour<8:
#N/S Cross section Henri 08.22 00z-21z
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lat2d[:,205:255], p2d[:,205:255],EPV[hour,:,205:255,188], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lat2d[:,200:250],p2d[:,200:250],EPV[hour,:,205:255,188],levels=[0.000002],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,254,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of EPV\n62.5W 08/15/21 {0:02.0f}z'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1


hour=0
while hour<8:
#E/W Cross section Odette 09.20 00z-21z
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,175:225], p2d[:,175:225],EPV[hour,:,269,175:225], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,175:225],p2d[:,175:225],EPV[hour,:,269,175:225],levels=[0.000002],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,254,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of EPV\n44.5 N 09/20/21 {0:02.0f}z'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

#E/W Cross section Melissa 10.09 00z-21z 
hour=0
while hour<8:
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('Greens')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[hour,:,256,150:200], 			levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[hour,:,256,150:200],levels=[0.1],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,257,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of RH\n38.5N 10/12/19 {0:02.0f}'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='RH')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

hour=0
while hour<8:
#E/W Cross section Henri 08.23 00z-21z
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,135:185], p2d[:,135:185],EPV[hour,:,263,135:185], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,135:185],p2d[:,135:185],EPV[hour,:,263,135:185],levels=[0.000002],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,254,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of EPV\n41.5N 08/23/21 {0:02.0f}'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

hour=0
while hour<8:
#E/W Cross section Henri 08.19 00z-21z
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[hour,:,240,150:200], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[hour,:,240,150:200],levels=[0.000002],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,254,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Henri Vertical Profile of EPV\n30N 08/20/21 {0:02.0f}'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

#E/W Cross section Melissa ET 10.09 PV 15z_Northern entity
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,155:205], p2d[:,155:205],EPV[5,:,256,155:205], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,155:205],p2d[:,155:205],EPV[5,:,256,155:205],levels=[0.000002],colors='black')
#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[2,:,239,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of PV Melissa\n38N 10/9/19 15Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
plt.show()


#E/W Cross section Melissa ET 10.14.19 PV 12z
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,200:250], p2d[:,200:250],EPV[4,:,262,200:250], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,200:250],p2d[:,200:250],EPV[4,:,262,200:250],levels=[0.000002],colors='black')
#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[2,:,239,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of PV Melissa\n41N 10/14/19 12Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
plt.show()


#Henri Origin 08.16.2021 EPV N/S cross section
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],EPV[3,:,200:300,188], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],EPV[3,:,200:300,188], levels=[0.000002],colors='black')
#wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,187],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of EPV Henri 08.16 06z 62.5W')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour:  Units = Tropopause')
plt.show()

Henri Origin 08.15.2021 EPV N/S cross section
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],EPV[2,:,200:300,188], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],EPV[2,:,200:300,188], levels=[0.000002],colors='black')
#wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,187],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of EPV Henri 08.15 06z 62.5W')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour:  Units = Tropopause')
plt.show()
'''
hour=0
while hour<6:
#E/W Cross section Melissa 10.12 00z-12
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[hour,:,257,150:200], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[hour,:,257,150:200],levels=[0.000002],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,254,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of EPV\n38.5N 10/11/19 {0:02.0f}z'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1
'''
hour=0
while hour<6:
#E/W Cross section Odette 09.18 00z-12
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[hour,:,254,150:200], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[hour,:,254,150:200],levels=[0.000002],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,254,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of EPV\n37N 9/18/21 {0:02.0f}'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

#E/W Cross section Melissa 10.12 00z-18z T
fig=plt.figure(figsize=[9,12])
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],T[0,:,256,150:200])			#levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	#cmap.set_over(color='black') #Sets values over the range as blacck
	#cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],T[0,:,256,150:200],colors='black')
#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[0,:,256,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
#plt.title('Vertical Profile of EPV\n33.5N 10/09/19 {0:02.0f}'.format(hour*3))
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
plt.show()
#E/W Cross section Melissa 10.10 00z-18z 
hour=0
while hour<7:
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('Greens')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[hour,:,256,150:200], 			levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[hour,:,256,150:200],levels=[0.1],colors='black')
	#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,257,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of RH\n38.5N 10/12/19 {0:02.0f}'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='RH')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

hour=0
while hour<3:
#E/W Cross section Melissa 10.12 00z-18z 
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[hour,:,256,150:200], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[hour,:,256,150:200],levels=[0.000002],colors='black')
	wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,256,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of EPV\n33.5N 10/09/19 {0:02.0f}'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

hour=0
while hour<7:
#E/W Cross section Odette 09.17 00z-18z 
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[hour,:,252,150:200], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[hour,:,252,150:200],levels=[0.000002],colors='black')
	wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,252,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of EPV\n36N 9/17/21 {0:02.0f}'.format(hour*3))
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[1,:,248,150:200],
levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[1,:,248,150:200], levels=[0.1],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], EPV[1,:,248,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of EPV\n36N 9/17/21 6Z')
plt.colorbar(cf, orientation='horizontal', label='RH')
plt.show()

#print file header info
#print(f)

#print the variables
#for v in f.variables:
#	print(v)

#print dimensions of the height variable
#print(f.variables['H'].dimensions)

##2D plot EPV data, y axis is height by pressure level, x axis is latitude
#E/W Cross section Henri 08.21.21 RH 12z: HURRICANE

cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[4,:,247,150:200], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[4,:,247,150:200], levels=[0.1],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], RH[4,:,247,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of Relative Humidity 08.21 12z Henri 33.5 N')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='RH')
plt.show()
hour=0
while hour<6:
#E/W Cross section Henri 08.21.21 PV 12z: HURRICANE
	fig=plt.figure(figsize=[9,12])
	cmap = plt.cm.get_cmap('RdPu')
	cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[hour,:,247,150:200], 			levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
	cmap.set_over(color='black') #Sets values over the range as blacck
	cmap.set_under(color='white') #Sets values under the range as white 
	plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[hour,:,247,150:200],levels=[0.000002],colors='black')
#wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[hour,:,247,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
	plt.gca().invert_yaxis()
	plt.xlabel('Longitude (Degrees)')
	plt.ylabel('Height/Level (hPa)')
	plt.title('Vertical Profile of PV\n33.5N 8/21/21 12Z')
	plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
	plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(hour))
	hour+=1

#E/W Cross section Henri TS 08.19.21 RH 06z
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[2,:,239,150:200], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[2,:,239,150:200], levels=[0.1],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], RH[2,:,239,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of Relative Humidity 08.19 06z Henri 29.5 N')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='RH')
plt.show()

#E/W Cross section Henri TS 08.19.21 PV 06z
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[2,:,239,150:200], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[2,:,239,150:200],levels=[0.000002],colors='black')
wind=plt.contour(lon2d[:,150:200], p2d[:,150:200], U[2,:,239,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of PV\n29.5N 8/19/21 6Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
plt.show()

#E/W Cross section Henri TS 08.18.21 RH near 15z
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[0,:,240,150:200], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[0,:,240,150:200], levels=[0.1],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], RH[0,:,240,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of Relative Humidity 08.18 Henri 63.75 N')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='RH')
plt.show()

#Henri 08.17.2021 RH N/S cross section
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],RH[0,:,200:300,185], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],RH[0,:,200:300,185], levels=[0.000002],colors='black')
wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,185],linestyles='dashed',colors='black')
plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of Relative Humidity 08.17 Henri 63.75 W')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='RH')
plt.show()
#E/W Cross section Henri TS 08.17.21 PV near 15z
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[5,:,238,150:200], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[5,:,238,150:200], levels=[0.000002],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], EPV[5,:,238,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of PV\n30.5N 8/17/21 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV')
plt.show()

#E/W Cross section Odette TS PV
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[1,:,248,150:200],
levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[1,:,248,150:200], levels=[0.1],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], RH[1,:,248,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of RH\n34N 9/17/21 3Z')
plt.colorbar(cf, orientation='horizontal', label='RH')
plt.show()

#E/W Cross section Henri TS 08.17.21 RH
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[0,:,238,150:200], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[0,:,238,150:200], levels=[0.000002],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], RH[0,:,238,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of RH\n71.4W 9/18/21 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()

#Henri Origin 08.15.2021 RH N/S cross section
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],RH[0,:,200:300,187], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],RH[0,:,200:300,187], levels=[0.000002],colors='black')
wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,187],linestyles='dashed',colors='black')
plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of Relative Humidity')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()

#Henri Origin 08.15.2021 PV N/S cross section
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],EPV[0,:,200:300,187], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],EPV[0,:,200:300,187], levels=[0.000002],colors='black')
wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,187],linestyles='dashed',colors='black')
plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
#plt.title('Vertical Profile of Ertel Potential Vorticity\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()

#Henri TD 08.16.2021 RH N/S cross section
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],RH[0,:,200:300,188], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],RH[0,:,200:300,188], levels=[0.000002],colors='black')
wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,188],linestyles='dashed',colors='black')
plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of Relative Humidity')#\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()

#Henri TD 08.16.2021 PV N/S cross section
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],EPV[0,:,200:300,188], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],EPV[0,:,200:300,188], levels=[0.000002],colors='black')
wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,188],linestyles='dashed',colors='black')
plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
#plt.title('Vertical Profile of Ertel Potential Vorticity\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()


#Odette TS PV
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],EPV[0,:,253,150:200], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],EPV[0,:,253,150:200], levels=[0.000002],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], EPV[0,:,253,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of RH\n71.4W 9/18/21 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()

#Odette Max Strength 09.20.21

fig1 = plt.figure(figsize=[8,5])
print(lon[202])
#Odette Max Strength
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],EPV[0,:,200:300,202], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],EPV[0,:,200:300,202], levels=[0.000002],colors='black')
vort=plt.contour(lat2d[:,200:300], p2d[:,200:300], EPV[0,:,200:300,202],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of Ertel Potential Vorticity\n53.75W 9/20/21 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()

#Odette TS 09.18.21 RH
cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lon2d[:,150:200], p2d[:,150:200],RH[0,:,253,150:200], levels=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lon2d[:,150:200],p2d[:,150:200],RH[0,:,253,150:200], levels=[0.000002],colors='black')
vort=plt.contour(lon2d[:,150:200], p2d[:,150:200], RH[0,:,253,150:200],linestyles='dashed',colors='black')
#plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Longitude (Degrees)')
plt.ylabel('Height/Level (hPa)')
plt.title('Vertical Profile of RH\n71.4W 9/18/21 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()


cmap = plt.cm.get_cmap('RdPu')
cf = plt.contourf(lat2d[:,200:300], p2d[:,200:300],EPV[0,:,200:300,201], levels=[0,0.000002,0.000004,0.000006,0.000008,0.00001,0.000012,0.000014,0.000016,0.000018,0.00002,0.000022,0.000024,0.000026,0.000028,0.00003],extend='both',cmap=cmap)
cmap.set_over(color='black') #Sets values over the range as blacck
cmap.set_under(color='white') #Sets values under the range as white 
plt.contour(lat2d[:,200:300],p2d[:,200:300],EPV[0,:,200:300,201], levels=[0.000002],colors='black')
wind=plt.contour(lat2d[:,200:300], p2d[:,200:300], U[0,:,200:300,201],linestyles='dashed',colors='black')
plt.clabel(wind,fmt='%1.0f',rightside_up='true')
#plt.contourf(EPV[7,:,272,:])
#plt.plot(lat,EPV[1,0])
plt.gca().invert_yaxis()
plt.xlabel('Latitude (Degrees North)')
plt.ylabel('Height/Level (hPa)')
#plt.title('Vertical Profile of Ertel Potential Vorticity\n148.8E 1/28/19 0Z')
plt.colorbar(cf, orientation='horizontal', label='$m^2 s ^{-1} K kg ^{-1}$\nBlack contour: 2 PV Units = Tropopause\nDashed contours: zonal wind U m/s')
plt.show()

#print(EPV[3])
#fig2= plt.figure()
#ax = plt.axes(projection='3d')
#ax.contour3D(lon2d,lat2d,PV, cmap='binary')
#plt.show()

#fig4 = plt.figure()
#ax = fig4.add_subplot(111, projection='3d')
#sp = ax.scatter(EPV[:,0],EPV[:,1],EPV[:,2])
#plt.colorbar(sp)
#plt. show()

#fig3 = plt.figure()
#ax = fig3.add_subplot(111, projection='3d')
#Z = np.linspace(0,42,num=43)
#PV = EPV[1]
#ax.plot_surface(EPV[:,3], EPV[:,2], EPV[:,1], rstride=1, cstride=1)#facecolors=cm.jet(PV/float(PV.max())))
plt.show()
'''

