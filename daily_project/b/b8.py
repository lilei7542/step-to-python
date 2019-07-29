import datetime as dt
  
def log_time(message, time=None):
  if time is None:
    time=dt.datetime.now()
  print("{0}: {1}".format(time.isoformat(), message))


log_time('now time')
# a=dt.datetime.now()

print (dt.date.day)
# print (dir(a))



# import spam
# print (spam.money)

# from spam import money,r1,r2
from spam import *
# money=10000000000
print (money)
r2()


import sys
print (sys.path)
