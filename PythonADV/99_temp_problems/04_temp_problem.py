import datetime
input_data_string = "8:00:00"
hh, mm, ss = input_data_string.split(":")
hh = int(hh)
mm = int(mm)
ss = int(ss)
a = datetime.datetime(1,1,1,hh,mm,ss)
b = a + datetime.timedelta(0,3) # days, seconds, then other fields.
print(a.time())
print(b.time())