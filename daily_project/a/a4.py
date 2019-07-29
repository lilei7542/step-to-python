# no.1
# from sys import getsizeof
# import sys
# sys.path.append('D:\\python_project\\module_myown')
# print (sys.path)

# no.2
print (dir())

# no.3      查看模块携带的函数~~~ verygood,see dir 
import math,sys
content = dir(math)
content2=dir(sys)
help(math)            #help dir       ---------->>>>>that's a good friend
# print (content,"\n",content2,"\n",content3) #"\n" 回车
