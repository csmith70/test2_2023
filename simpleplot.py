import numpy as np
import matplotlib.pyplot as plt
import LHD
import statsmodels.api as sm

file_in = LHD.load_space_data('ozone_fit_regression_input.dat', 2)
year = file_in[:,0]
obs_o3 = file_in[:,1]
modelO3 = file_in[:,2]
tsi = file_in[:,3]
halo = file_in[:,4]
aero = file_in[:,5]
qbo = file_in[:,6]

# Defines the number of observations and regressors 
nobs = len(year)  # Number of observations
nrgs = 5 # Number of regressors + 1 (1 is for the y-intercept const.) 

# Create a matrix of 1s with the dimentions defined above
regressors = np.ones((nobs,nrgs), dtype=np.float)


# Populate the matrix columns with regressors (leaving column 0 as 1s) 
regressors[:,1] = tsi
regressors[:,2] = halo
regressors[:,3] = aero
regressors[:,4] = qbo

# Create an ordinary least squares model
model = sm.OLS(obs_o3, regressors)
# Extract the constants
constants = model.fit().params
print(constants)
# Calculate the model fit result
model_o3 = constants[0] + constants[1]*tsi + constants[2]*halo + constants[3]*aero + constants[4]*qbo

# Plot
plt.plot(year, obs_o3, c='g', label = 'Observed') # Observations
plt.plot(year, model_o3, c='r', lw=1, label = 'MLR w/ Python') # MLR with Python

plt.xlabel('Year')
plt.ylabel('Column Ozone Anomaly (DU)')
plt.legend()
 

plt.show()

t = np.arange(0,1,0.5)
s = t*4
p = t*1
xmin = 0
xmax = 5
#Set up axis parameters
left = 0.2
base = 0.1
base_top = 0.7
del_base = 0.2
width = 0.7
height = 0.15
#fig = plt.figure()
#Set up parameters for plotting axes for plots
fig = plt.figure(figsize=[9,12])
ax1 = fig.add_axes([left, base_top, width, height])
ax2 = fig.add_axes([left, base+del_base*2, width, height])

print('____Summary_____')
print(model.fit().summary())

#ax1  = fig.add_subplot(111)
ax1.set_xlim(xmin, xmax)
ax2.set_xlim(xmin,xmax)
ax1.plot(t,s, color='g')
ax2.plot(t,p, color='r')
ax2.set_xlabel('Time (s)')
ax1.set_ylabel('y value')
ax2.set_ylabel('y value')
plt.legend(loc = 0)
#plt.show()
print(year)
