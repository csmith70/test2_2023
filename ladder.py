## Christopher Smith
## HW 5: Ladder Plot and CSV Output
## 9/18/19

#Import modules
import numpy as np
import matplotlib.pyplot as plt
import LHD

#Load NASA text data using LHD module
data_in = LHD.load_space_data('graph.txt.1', 9)
#Get years data (all the rows and first column)
years = data_in[:, 0]
print(years)

#Get global temps data (all the rows and second column)
glob_temps = data_in[:, 1]
print(glob_temps)

#Get northern hemisphere temps data (all the rows and third column)
NHem_temps = data_in[:, 2]
print(NHem_temps)

#Get southern hemisphere temps data (all the rows and fourth column)
SHem_temps = data_in[:, 3]
print(SHem_temps)

#Get 24S to 24N temps data (all the rows and sixth column)
S_toNorth = data_in[:,5]
print(S_toNorth)

#Set up axis parameters
left = 0.2
base = 0.1
base_top = 0.7
del_base = 0.2
width = 0.7
height = 0.15

#Set up x axis limits using year min/max 
xmin = min(years)
xmax = max(years)

#Set up parameters for plotting axes for plots
fig = plt.figure(figsize=[9,12])
ax1 = fig.add_axes([left, base_top, width, height])
ax2 = fig.add_axes([left, base+del_base*2, width, height])
ax3 = fig.add_axes([left, base+del_base, width, height])
ax4 = fig.add_axes([left, base, width, height])

#Remove tick labels from first three x-axes
ax1.xaxis.set_ticklabels([])
ax2.xaxis.set_ticklabels([])
ax3.xaxis.set_ticklabels([])

#Set all x-axes to same range
ax1.set_xlim(xmin, xmax)
ax2.set_xlim(xmin, xmax)
ax3.set_xlim(xmin, xmax)
ax4.set_xlim(xmin, xmax)

#Set ticks for y-axes
ax1.yaxis.set_ticks(np.arange(-.75, 1.75, 0.25))
ax2.yaxis.set_ticks(np.arange(-.75,1.75, 0.25))
ax3.yaxis.set_ticks(np.arange(-.75, 1.75, 0.25))
ax4.yaxis.set_ticks(np.arange(-.75, 1.75, 0.25))

#Plot the data
ax1.plot(years, glob_temps, c='r')
ax2.plot(years, NHem_temps, c='g')
ax3.plot(years, SHem_temps, c='k')
ax4.plot(years, S_toNorth, c='b')

#Set Y labels
ax1.set_ylabel('Temperature\nAnomaly\n(C)')
ax2.set_ylabel('Temperature\nAnomaly\n (C)')
ax3.set_ylabel('Temperature\nAnomaly\n (C)')
ax4.set_ylabel('Temperature\nAnomaly\n (C)')

ax4.set_xlabel('Years')

#Set titles for each plot
fig.suptitle('Mean Land-Ocean Temperature Anomaly in\n Degrees C Per Region')
ax1.set_title('Global Temperature Anomalies')
ax2.set_title('Northern Hemisphere Temperature Anomalies')
ax3.set_title('Southern Hemisphere Temperature Anomalies')
#Account for degree symbol
ax4.set_title('Temperature Anomalies (24$^\circ$S to 24$^\circ$N)')

plt.show()

#Import all the temperature data for the csv plot
temps = data_in[:,:]
print(temps)

#Save numpy array as csv file that matches data plotted with headers
HEADER = "Annual mean Land-Ocean Temperature Index in degrees Celsius\n selected zonal means\nYear  Glob   NHem   SHem  24S\n                         -24N"
#Delimeter = ',' and save file as csv due to type of file specified
np.savetxt('Tanom.csv', temps[:,[0,1,2,3,5]], fmt='%1.2f', delimiter=',', header = HEADER)






