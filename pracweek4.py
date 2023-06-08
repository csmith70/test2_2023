import netCDF4

filename = 'start08_rf01_AWAS_merged_final_v03.nc'
f = netCDF4.Dataset(filename, mode='r')  # Read file into f
