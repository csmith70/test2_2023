import numpy as np
import matplotlib.pyplot as plt
import LHD
import MyFunctions as mf
import pandas as pd
import matplotlib.dates as mdates
import datetime

data_in = LHD.load_comma_data('NBM.csv', 2)
df = pd.DataFrame(data_in)
time = data_in[:,0]
burg = data_in[:,1]
burg = burg[~pd.isnull(burg)]
#print(burg)
gtown = data_in[:,2]
gtown = np.array(gtown)
gtown = gtown[~pd.isnull(gtown)]
easton = data_in[:,3]
easton = np.array(easton)
easton = easton[~pd.isnull(easton)]
OC = data_in[:,4]
oc = np.array(OC)
oc = oc[~pd.isnull(oc)]
dover = data_in[:,5]
dover = np.array(dover)
dover = dover[~pd.isnull(dover)]
bury = data_in[:,6]
bury=np.array(bury)
bury = bury[~pd.isnull(bury)]
temp=burg+gtown+easton+oc+dover+bury
tempv = np.array(temp)
npts = len(burg)*6
MAE = []

i = 1
total=0
total2=0
while i < 21:
	if (i % 2) != 0:
		difference = (tempv[i] - tempv[i-1]) 
		MAE.append(difference)
		temperature = tempv[i]
		total = total+temperature
		#print(difference)
		print(total)
	if (i%2) == 0:
		temperature2 = tempv[i]
		total2 = total2 + temperature2
	i+=1

#print(oc)
#******OC Case Study*****
i=1
ocMAE=[]
while i < 21:
	if (i%2) !=0 :
		differenceOC = (oc[i]-oc[i-1])
		ocMAE.append(differenceOC)
	i+=1
print(0-sum(ocMAE)/len(oc))

#******Georgetown Case Study*****
i=1
gtownMAE = []
while i < 21:
	if (i%2) !=0 :
		differenceGTOWN = (gtown[i]-gtown[i-1])
		gtownMAE.append(differenceGTOWN)
	i+=1

i=1
gtownv = []
gtownp = [] #georgetown predicted
while i < 21:
	if (i%2) != 0:
		gtownv.append(gtown[i])
	if(i%2) == 0:
		gtownp.append(gtown[i])
	i+=1
print(gtownv)
print(gtownp)
print(0-sum(gtownMAE)/len(gtown))

dates = ["05/28/12/2020", "05/28/14/2020", "05/28/16/2020","05/29/10/2020", "05/29/12/2020", "05/29/14/2020","05/29/16/2020","06/01/10/2020","06/01/12/2020","06/01/14/2020"]#"06/01/16/2020"]
#convert to datetime

x_values = [datetime.datetime.strptime(d,"%m/%d/%H/%Y").date() for d in dates]
print(x_values)
#y_values = [1,2,3,4,5,6,7,8,9,10]
#y_values = [77,82,82,80,84,86,80,64,67,70]
a = np.array(gtownv)
b = a.flatten()
y_values=[b]
c = np.array(gtownp)
d = c.flatten()
y_valuesp = [d]
ax = plt.gca()
#get axes


formatter = mdates.DateFormatter("%Y-%m-%d-%H")
#format as dates

ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()
#set locator

ax.xaxis.set_major_locator(locator)

plt.scatter(x_values,y_values, c='b',label='Recorded T')
plt.scatter(x_values, y_valuesp, c='g', label='Predicted T')
plt.xlabel('Time')
plt.ylabel('Temperature in Degrees F')
plt.title('NBMV4.0 Verification for Georgetown, DE')
plt.legend(loc=0)
plt.show()
#plot values
plt.plot(gtownv, color='b',label='Recorded T')
plt.plot(gtownp, color='g', label='Predicted T')
plt.legend(loc=0)
plt.xlabel('Time')
plt.ylabel('Temperature in Degrees F')
plt.title('NBMV4.0 Verification for Georgetown, DE')
plt.show()

#print(MAE)
#difference = int(difference)
print(0-(sum(MAE)/npts))
#MAE = sum(difference)/npts

