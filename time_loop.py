#LST Loop 

import numpy as np 
import datetime as dt
import time
import h5py

start_time = time.time()
curDT = dt.datetime(2009,6,1,00,00)
endDT = dt.datetime(2009,6,30,23,50)
StYear = curDT.strftime("%Y")
StMonth = curDT.strftime("%m")
StDay = curDT.strftime("%d")
row = 486 
column = 680
LST_Series = []
good = 0
bad = 0
path = '/data/studentdata/jeff/Europe/'
while curDT < endDT:
	year = curDT.strftime("%Y")
	file = path + year + "/HDF5_LSASAF_MSG_LST_Euro_" + curDT.strftime("%Y%m%d%H%M")
	print(file)
	try:
		f = h5py.File(file,mode='r')
		#print('file')
		LST = f['LST'][row,column]
		#print('LST')
		QFLAGS = f['Q_FLAGS'][row,column]
		#print('Q_Flag')
		#ERROR = f['errorbar_LST'][:,:]
		LST_Series.append([LST,QFLAGS,int(curDT.strftime("%Y%m%d%H%M"))])
		#print('Append')
		good += 1
		#print(curDT)
	except:
		print('No File')
		LST_Series.append([-9999,-9999,int(curDT.strftime("%Y%m%d%H%M"))])
		bad += 1
		#pass
	EndYear=curDT.strftime("%Y")
	EndMonth=curDT.strftime("%m")
	EndDay=curDT.strftime("%d")
	curDT = curDT + dt.timedelta(minutes=15)

print(np.shape(LST_Series))
#print(LST_Series)
#EndYear=curDT.strftime("%Y")
outfile = "LST_{0}{1}{2}-{3}{4}{5}-{6}-{7}.csv".format(StYear,StMonth,StDay,EndYear,EndMonth,EndDay,row,column)
np.savetxt(outfile, LST_Series, delimiter=',', header='LST, Quality Flags, Datetime\n'+year, fmt='%d')

elapsed_time = time.time() - start_time
print("Time Elapsed: "+str(elapsed_time))
print("Good Files: {}".format(good))
print("Missing Files: {}".format(bad))

