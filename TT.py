from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import LHD
from matplotlib.lines import Line2D

legend_elements = [Line2D([0], [0], marker='o', color='w', label='Prior to June',
                          markerfacecolor='r', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Summer',
                          markerfacecolor='b', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Fall',
                          markerfacecolor='g', markersize=10)]

# Create the figure
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')

plt.show()
df = pd.read_csv("TT.csv", delimiter=',', skiprows=0, low_memory=False)

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)   
print(gdf['Month'])
print(type(gdf['Month']))
a = list(gdf['Month'])
b=list(gdf['SST'])
RH=list(gdf['RH'])
T=list(gdf['200T'])
print(RH)
'''
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.set_global()
gdf.plot(ax=ax, color='red')

plt.show()
'''

# Function to map the colors as a list from the input list of x variables
def pltcolor(lst):
    cols=[]
    for l in lst:
        if l=='January' or l == 'April' or l =='May':
            cols.append('red')
        elif l=='June' or l == 'July' or l =='August':
            cols.append('blue')
        else:
            cols.append('green')
    return cols
# Create the colors list using the function above
cols=pltcolor(a)
print(cols)
proj = ccrs.PlateCarree(central_longitude=0)
fig = plt.figure(figsize=[5, 8])
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines()
plt.title('Binning TT by Month/Season')
# original ax.set_extent((-120, 120, -45, 45)) ?
# Need longitude extent from -60 to +60 on PlateCarree(central_longitude=180)
minlon = -60 + -30
maxlon = 60 + -30
ax.set_extent([minlon, maxlon,0,75]), ccrs.PlateCarree()
ax.gridlines(draw_labels=True, crs=proj)
#gdf.plot(ax=ax, c=gdf['month')
#gdf.plot(ax=ax,column='Month',legend=True)
gdf.plot(ax=ax,c=cols)
ax.legend(handles=legend_elements, loc=0)
#gdf.plot(ax=ax,c=cols)
plt.show()

legend_elements = [Line2D([0], [0], marker='o', color='w', label='26C+',
                          markerfacecolor='r', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='<26C',
                          markerfacecolor='b', markersize=10)]

def pltcolor1(lst):
    cols=[]
    for l in lst:
        if l<28:
            cols.append('blue')
        else:
            cols.append('red')
    return cols
# Create the colors list using the function above
cols=pltcolor1(b)
print(cols)
proj = ccrs.PlateCarree(central_longitude=0)
fig = plt.figure(figsize=[5, 8])
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines()
# original ax.set_extent((-120, 120, -45, 45)) ?
# Need longitude extent from -60 to +60 on PlateCarree(central_longitude=180)
minlon = -60 + -30
maxlon = 60 + -30
ax.set_extent([minlon, maxlon,0,75]), ccrs.PlateCarree()
ax.gridlines(draw_labels=True, crs=proj)
gdf.plot(ax=ax,c=cols)
plt.title('SST During TT')
ax.legend(handles=legend_elements, loc=0)
#gdf.plot(ax=ax,c=cols)
plt.show()

def pltcolor2(lst):
    cols=[]
    for l in lst:
        if l<50:
            cols.append('brown')
        else:
            cols.append('green')
    return cols
cols=pltcolor2(RH)
print(cols)
proj = ccrs.PlateCarree(central_longitude=0)
fig = plt.figure(figsize=[5, 8])
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines()

# original ax.set_extent((-120, 120, -45, 45)) ?
# Need longitude extent from -60 to +60 on PlateCarree(central_longitude=180)
minlon = -60 + -30
maxlon = 60 + -30
ax.set_extent([minlon, maxlon,0,75]), ccrs.PlateCarree()
ax.gridlines(draw_labels=True, crs=proj)
#gdf.plot(ax=ax, c=gdf['month')
gdf.plot(ax=ax,c=cols)
plt.show()

def pltcolor3(lst):
    cols=[]
    for l in lst:
        if l<-50:
            cols.append('blue')
        else:
            cols.append('red')
    return cols
cols=pltcolor3(T)
print(cols)
proj = ccrs.PlateCarree(central_longitude=0)
fig = plt.figure(figsize=[5, 8])
ax = fig.add_subplot(1, 1, 1, projection=proj)
ax.coastlines()

# original ax.set_extent((-120, 120, -45, 45)) ?
# Need longitude extent from -60 to +60 on PlateCarree(central_longitude=180)
minlon = -60 + -30
maxlon = 60 + -30
ax.set_extent([minlon, maxlon,0,75]), ccrs.PlateCarree()
ax.gridlines(draw_labels=True, crs=proj)
#gdf.plot(ax=ax, c=gdf['month')
gdf.plot(ax=ax,c=cols)
plt.show()

