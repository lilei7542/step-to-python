from datetime import *
import pytz
# print (dir(datetime.now))
z=datetime.now(tz=pytz.timezone('Asia/Chongqing'))
j=datetime.now()
print (z)
print (j)
l=pytz.timezone('Asia/Chongqing')
print (l)
# m=datetime.dst()
a=dir(pytz.tzinfo) 
print(a)


