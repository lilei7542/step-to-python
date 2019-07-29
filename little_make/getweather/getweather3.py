# -*- coding: utf-8 -*-
#version 1.2

import requests
import json


url_r='https://api.seniverse.com/v3/weather/now.json?key=kfkzrgn2ygbu92ce&location=XIAN&language=zh-Hans&unit=c'


# from request import *

import getweather5

# from urllib.request import *

data_2=requests.get(url_r)
data_3=data_2.json()
data_4=str(data_3)

data_6=json.dumps(data_3)
data_7=json.loads(data_6)
print (type(data_2))
print (data_3['results'])


print (type(data_6))
print (type(data_7))



with open ('D:\\python_project\\experimental_data\\1','w+') as f1:
	# f1.write(data_4)  #写为str格式，不行，还得改
	f1.write(data_6)  	#写为str格式，json.dumps转化的，ok
	f1.close()

# with open ('D:\\python_project\\experimental_data\\1','rb') as f2:
# 	c=f2.readline()
# 	f2.close()

