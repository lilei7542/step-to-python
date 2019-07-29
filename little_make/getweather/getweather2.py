# -*- coding: utf-8 -*-
#version 1.1

url_r='https://api.seniverse.com/v3/weather/now.json?key=kfkzrgn2ygbu92ce&location=XIAN&language=zh-Hans&unit=c'

import urllib
import request
from urllib.request import *



# a=urllib.request.urlopen(url_r)
# data_1=a.read()

# print (dir (a))
# print (type (a))

# print (a.readline())
# print (a.read())


data_2=urllib.request.urlopen(url_r)
data_3=data_2.read()
print (type(data_2))
print (type(data_3))

with open ('D:\\python_project\\experimental_data\\1','wb+') as f1:
	f1.write(data_3)
	f1.close()

with open ('D:\\python_project\\experimental_data\\1','rb') as f2:
	c=f2.readline()
	f2.close()

print (c)