## Christopher Smith
## HW6
## 9/24/19

#Import Modules
import LHD
import numpy as np
import matplotlib.pyplot as plt

#Load data using LHD csv load data function 
data_in = LHD.load_comma_data('planets.csv', 148)

#Make array of Stellar Mass loading all the rows and the 30th column of data
st_mass = data_in[:,29]
print(st_mass)
#Make blank values in array 'NaN'
st_mass[np.where(st_mass=='')]='NaN'
#Get max value of stellar mass, ignoring NaN values
a = np.nanmax(st_mass)
print(a)

#Make array of Planet Mass loading all the rows and the 12th column of data 
pl_bmass = data_in[:,11]
#Make blank values in array 'NaN'
pl_bmass[np.where(pl_bmass=='')]='NaN'
#Get max value of planet mass, ignoring NaN values
b = np.nanmax(pl_bmass)
print(b)

#Make array that masks values of planet mass less than or equal to 70% of planet maximum mass
pl_upper = np.ma.masked_where(pl_bmass <= (0.7*b), pl_bmass)
print(pl_upper)
#Make array that masks values of planet mass above 70% of planet maximum mass
pl_lower = np.ma.masked_where(pl_bmass > (0.7*b), pl_bmass)

#Plot scatterplot with two different specified colors for pl_upper and pl_lower. Include axes labels and title
fig = plt.figure()
ax1  = fig.add_subplot(111)
ax1.scatter(st_mass, pl_upper, color = 'r', label = 'Greater Than 70% of Max. Mass')
ax1.scatter(st_mass, pl_lower, color = 'k', label = '70% of Max. Mass or Less ')
plt.title('Planet Mass v Stellar Mass')
plt.legend(loc = 0)
plt.xlabel('Stellar Mass (Units: Solar Mass)')
plt.ylabel('Planet Mass(Units: Jupiter Mass)')
plt.show()

## Make a Histogram of Planet Mass Data with 10 bins. Include axes labels and title
n, bins, patches = plt.hist(pl_bmass, 10, normed=True)
plt.ylabel('Frequency')
plt.xlabel('Planet Mass(Units:Jupiter Mass)')
plt.title('Histogram of Planet Mass')
plt.show()










