import datetime as dt

date_string = "21 June, 2018"
print("date_string = " + date_string)
date_object = dt.datetime.strptime(date_string, "%d %B, %Y")
print("date_object = {0}".format(date_object))

