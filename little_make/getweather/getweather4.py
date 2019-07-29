# -*- coding: utf-8 -*-
#version 1.3

import requests
import json
import sys

# url_r='https://api.seniverse.com/v3/weather/now.json?key=kfkzrgn2ygbu92ce&location=XIAN&language=zh-Hans&unit=c'

# data_4=str(data_3)
# data_6=json.dumps(data_3)
# data_7=json.loads(data_6)

# print (type(data_2))
# print (data_3['results'])
# print (type(data_6))
# print (type(data_7))


def main():

	location=sys.argv[1] 		#sys.argv[0]表示代码本身文件路径,所以从参数1开始,表示获取的参数了

	url_r='https://api.seniverse.com/v3/weather/now.json?key=kfkzrgn2ygbu92ce&location='+location+'&language=zh-Hans&unit=c'

	data_2=requests.get(url_r)

	data_3=data_2.json()


	print (data_3['results'])
	# print (data_3)







if __name__=='__main__':
	main()
	# print ('abc')

#usage->:	cmd ->  getweather4.py xian
