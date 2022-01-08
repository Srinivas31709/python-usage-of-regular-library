import datetime
import time
import calendar
print(time.time())
print(time.asctime())
print(time.asctime(time.localtime(time.time())))
datetime_object = datetime.datetime.now()
print(datetime_object)
print("Year: ", datetime_object.year)
s = calendar.prcal(2022)
s = calendar.prcal(2023)

print(s)