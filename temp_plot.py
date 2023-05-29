## Christopher Smith
## HW 4: ASCII Input and Plotting Running Means
## Part 1
## 9/15/19

#import modules
import numpy as np
import matplotlib.pyplot as plt
import LHD

#Load gloabl temperature record data and skip 8 lines of header
data_in = LHD.load_space_data('global_temp_rec.dat', 8)
# Mask data that is not relevant to set 
masked_data = np.ma.masked_where(data_in == -999., data_in)
print(masked_data)

# Print all the rows and the first column of data (years)
years = masked_data[:,0]
# Print all the rows and the second column of data (temps)
temps = masked_data[:,1]

#Create a running mean function of temperature over a scale of 5 successive years 
def running_mean (years, temps, n = 5):
	#Make sure the years and temps data are of same length
	if len(years) != len(temps):
		print('years and temps must be of equal length')
		return None, None
n = 5
#Calculate the cumulative sum of years
yearsx = np.cumsum(years, dtype = float)
#Calculate the cumulative sum within the defined window
yearsx[n:] = yearsx[n:] - yearsx[:-n]
# Calculate the mean within the defined window
yearsx = yearsx[n-1:]/n

#Calculate the cumulative sum of temperatures
tempsy = np.cumsum(temps, dtype = float)
#Calculate the cumulative sum within the defined window
tempsy[n:] = tempsy[n:] - tempsy[:-n]
# Calculate the mean within the defined window
tempsy = tempsy[n-1:]/n
# Check the values by printing them out
print(yearsx, tempsy)

#Plot temps v years with defined linestyle, color, marker style, and label
plt.plot(years, temps, ls="--", color = 'red', marker = "*", label = "Original Data")
# Plot temps v years running mean with new color
plt.plot(yearsx, tempsy, ls = "-", color = "green", marker = "", label = "Running Mean")
#Plot title, labels, and the legend in the best location
plt.title("Global Temp Anomalies")
plt.xlabel("Years")
plt.ylabel("Temperature Anomalies \nin C")
plt.legend(loc = 0)
#Show the plot
plt.show()


