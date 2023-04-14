## Christopher Smith
## HW4: ASCII Input and Plotting Running Means
## Part 2
## 9/15/19

#Import modules
import numpy as np
import matplotlib.pyplot as plt
import LHD

#Import data from csv file using LHD load comma data function, skip 2 lines of header 
data_in = LHD.load_comma_data('graph.csv', 2)
print(data_in)

#Import and print all the rows of data and the first column (years)
years = data_in[:,0]
print(years)

#Import and print all the rows of data and the second column (temps)
temps = data_in[:,1]
print(temps)

#Import the lowess 5 year running mean from NASA (all rows and third column of data)
lowess = data_in[:,2]

#Define the 5 year running mean function
def running_mean (years, temps, n=5):
	# Make sure the length of data temps v years are equal
	if len(years) != len(temps):
		print('Years and temps must be of equal length')
		return None, None

n = 5
#Calculate the cumulative sum of years
yearx = np.cumsum(years, dtype = float)
#Calculate the cumulative sum of years within the 5 year smoothing window
yearx[n:] = yearx[n:] - yearx[:-n]
# Calculate the average within the window
yearx = yearx[n-1:]/n

#Calculate the cumulative sum of temperatures
tempy = np.cumsum(temps, dtype = float)
#Calculate the cumulative sum of temperatures within the 5 year smoothing window
tempy[n:] = tempy[n:] - tempy[:-n]
#Calculate the average within the window
tempy = tempy[n-1:]/n
# Check the data by printing it out
print(yearx,tempy)

#Plot temps v years, NASA 5-Year Lowess Smoothing v years, and Calculated 5 year running mean v years on the same graph 
#Use different styles (color, or line, etc.) 
plt.plot(years, temps, ls = "--", color = "red", marker = "*", label = "Original Data")
plt.plot(years, lowess, ls = "-", color = "green", marker = "", label = "NASA 5-Year Lowess Smoothing")
plt.plot(yearx, tempy, ls = "-", color = "blue", marker = "", label = "Calculated 5-Year Running Mean")
#Plot title and labels as well as legend in location with most white space
plt.title("US Temperature (Annual Mean)")
plt.xlabel("Years")
plt.ylabel("Temperature Anomalies \nin C")
plt.legend(loc = 0)
plt.show()
