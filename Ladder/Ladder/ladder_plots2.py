# data file: ozone_fit_regression_components.dat
# Data Columns:
### 0 time
### 1 observed_ozone_NIWA(DU)
### 2 modeled_ozone(DU)
### 3 tsi_impact(DU)
### 4 halogen_impact(DU)
### 5 aerosol_impact(DU)
### 6 QBO_30mb_impact(DU)
### 7 residual(DU)

import LHD
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# Load Data into array
data_in = LHD.load_space_data('ozone_fit_regression_components.dat',2)
data_in = np.ma.masked_where(data_in == -999, data_in) # hides -999
data_in = np.ma.compress_rows(data_in) #Deletes any row containing -999

# Assign base variables
time = data_in[:,0]
obsOzone = data_in[:,1]
modOzone = data_in[:,2]
tsiImpact = data_in[:,3]
halogenImpact = data_in[:,4]
aerosolImpact = data_in[:,5]
QBOImpact = data_in[:,6]
residual = data_in[:,7]

fig1 = plt.figure(figsize=[9,12])

#Set plot Grid
ax1 = plt.subplot2grid((8,1), (0,0), rowspan=2)
plt.setp(ax1.get_xticklabels(), visible=False)

ax2 = plt.subplot2grid((8,1), (3,0))
plt.setp(ax2.get_xticklabels(), visible=False)

ax3 = plt.subplot2grid((8,1), (4,0))
plt.setp(ax3.get_xticklabels(), visible=False)

ax4 = plt.subplot2grid((8,1), (5,0))
plt.setp(ax4.get_xticklabels(), visible=False)

ax5 = plt.subplot2grid((8,1), (6,0))
plt.setp(ax5.get_xticklabels(), visible=False)

ax6 = plt.subplot2grid((8,1), (7,0))

# Plotting data
ax1.plot(time,obsOzone,c='g')
ax2.plot(time,residual,c='k')
ax3.plot(time,tsiImpact,c='r')
ax4.plot(time,halogenImpact,c=(.6,0,0.6))
ax5.plot(time,aerosolImpact,c='b')
ax6.plot(time,QBOImpact,c=(.6,.6,0))

#plt.tight_layout()
ax1.set_title('Column Ozone Anomaly (55$^\circ$S to 55$^\circ$N)')
ax2.set_title('Predictor Variables X Regression Coefficients')
ax1.set_ylabel('Column Ozone\nAnomaly (DU)')
ax2.set_ylabel('Residuals')
ax3.set_ylabel('TSI (DU)')
ax4.set_ylabel('Halogens\n(DU)')
ax5.set_ylabel('Sulfate\nSurface\nArea (DU)')
ax6.set_ylabel('QBO (DU)')

plt.show()
