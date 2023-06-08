#+
# NAME: hw4.py
#
# AUTHOR: XXXXXXXXX
#
# PURPOSE: read in ASCII data using the LHD module
#	   compute the 5-year running mean
#
# EDITED: 09/14/2018 @4:37pm
# EDITED: 09/19/2018 @11:15am to add MyFunctions module
#---------------------------------------------------------

# importing modules 

import numpy as np
import matplotlib.pyplot as plt
import LHD
import MyFunctions as mf

##########################################################
#                                                        #
#                     MAIN PROGRAM                       #
#                                                        #
##########################################################

# Load data using LHD and then mask -999 data
data_in = LHD.load_space_data('global_temp_rec.dat',8)
masked_data = np.ma.masked_where(data_in == -999, data_in)

years = masked_data[:,0] #grabs all rows in the first column
temp  = masked_data[:,1] #grabs all rows in the second column

#compute 5-year running mean
'''
rmean = []  #empty values added to beginning of running mean

x=2
while x< 136:

	#calculate running mean
	total = (temp[x]+temp[x-1]+temp[x-2]+temp[x+1]\
		 +masked_data[x+2])/5
	
	#round the mean to 2 decimal places
	mean = float(round(total[1],2))

	#add mean to the end of existing array
	rmean.append(mean)	
	x+=1
'''
rmean,window = mf.running_mean(temp,5)

#### Begin Plotting ####
plt.plot(years,temp,ls="-",color="b",marker="*",label="Original Data")  #plots the temp data
plt.plot(years[2:-2],rmean[2:-2],ls="-",color="r",label="5-yr Running Mean")
plt.title("Global Temperature Anomalies")                               #make graph title
plt.hlines(0,years[0],years[-1])                                        #make zero line
plt.xlabel("Years")                                                     #make graph x-axis title
plt.ylabel("Temperature Anomalies\nin C")                               #make graph y-axis title
plt.legend(loc=0)
plt.show()                                    #shows the plot in a separate window





