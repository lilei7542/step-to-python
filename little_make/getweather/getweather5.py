# -*- coding: utf-8 -*-
#version 1.3

import requests
import json
import sys


def getarg():
	location_1=sys.argv 		#sys.argv[0]表示代码本身文件路径,所以从参数1开始,表示获取的参数了
	location_default='beijing'
	if len(location_1) >=2:
		location=location_1[1]
	else:
		location=location_default
	return location



def main():

	location=getarg()

	url_r='https://api.seniverse.com/v3/weather/now.json?key=kfkzrgn2ygbu92ce&location='+str(location)+'&language=zh-Hans&unit=c'

	data_2=requests.get(url_r)

	data_3=data_2.json()


	# print (data_3['results'])
	print (data_3)







if __name__=='__main__':
	main()
	# print ('abc')

#usage->:	cmd ->  getweather4.py xian
