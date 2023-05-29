import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import LHD

data_in = LHD.load_space_data('location.dat',1)
lat = data_in[:,0]
#print(lat)
lon = data_in[:,1]
pg = []
ph = []
issue = 0 
while issue < 5:
	fig=plt.figure(figsize=[9,12])
	px = lat[issue]
	pg.append(px)
	#print(px)
	py = lon[issue]
	ph.append(py)
	#print(py)
	m = Basemap(llcrnrlon=-95,llcrnrlat=22,urcrnrlon=-85,urcrnrlat=31,
            projection='lcc',resolution='h', lat_1 = 25.9, lon_0=-89.7)
	m.shadedrelief()
	pm,pb=m(ph,pg)
	plt.plot(pm,pb,marker='*',markersize=9,color='blue')
	#plt.show()
	fig.savefig('plot{0:03.0f}.png'.format(issue))
	issue += 1
print(pg)
'''
#Plot MD cities on a map for snow winners, losers, reference
m = Basemap(llcrnrlon=-95,llcrnrlat=22,urcrnrlon=-85,urcrnrlat=30,
            projection='lcc',resolution='h', lat_1 = 25.9, lon_0=-89.7)
m.shadedrelief()
px, py = m(-89.70, 25.90) #Waves_Verification_25N
pg, ph = m(-90.20, 23.90) #Cristobal Saturday, June 6, 8a.
pm, pb = m(-92, 28) #25N label
plt.plot(px, py, marker = '*',markersize=9,color ='blue')
plt.plot(pg, ph, marker = 'o',markersize=9,color ='black')
plt.text(pm, pb, 'Location 25N', fontsize = 8, fontweight = 'bold', bbox=dict(facecolor='white', edgecolor='black'))
plt.show()
'''
