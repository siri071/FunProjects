import calendar

cal = calendar.month(2022, 1)
print("Here is the calendar:")
print(cal)

import time;

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)