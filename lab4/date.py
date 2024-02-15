#a program that substracts five days from current date
from datetime import date, timedelta
next = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',next)


#a program that prints yesterday, today, tomorrow
from datetime import date, timedelta
yesterday = date.today() - timedelta(1)
tomorrow = date.today() + timedelta(1)
print('Yesterday :',yesterday)
print('Current Date :',date.today())
print('Tomorrow :',tomorrow)

#a program that drops microseconds from datetime
import datetime
time = datetime.datetime.today().replace(microsecond=0)
print()
print(time)
print()

#calculate two date difference in seconds
from datetime import datetime, time
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime(input("Enter date "), '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
print()