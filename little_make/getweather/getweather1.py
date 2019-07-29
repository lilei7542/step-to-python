# {
# "results":
# 	[
# 		{
# 		"location":
# 			{
# 				"id":"WX4FBXXFKE4F","name":"北京","country":"CN","path":"北京,北京,中国","timezone":"Asia/Shanghai","timezone_offset":"+08:00"
# 			},
# 		"now":
# 			{
# 				"text":"多云","code":"4","temperature":"27"
# 			},
# 		"last_update":"2018-09-12T16:00:00+08:00"
# 		}
# 	]
# }		




z={
  "results": [{
  "location": {
      "id": "C23NB62W20TF",
      "name": "西雅图",
      "country": "US",
      "timezone": "America/Los_Angeles",
      "timezone_offset": "-07:00"
  },
  "now": {
      "text": "多云",
      "code": "4",
      "temperature": "14",
      "feels_like": "14",
      "pressure": "1018",
      "humidity": "76",
      "visibility": "16.09",
      "wind_direction": "西北",
      "wind_direction_degree": "340",
      "wind_speed": "8.05",
      "wind_scale": "2",
      "clouds": "90",
      "dew_point": "-12"
  },
  "last_update": "2015-09-25T22:45:00-07:00"
  }]
}

print (z)

# a={{'b':'d'}:{'c':'e'}}
a={'mn':{'c':'e'}}
b={'mn':['a','b']}



# print "dict['Age']: ", dict['Age'];



print (z['results'])

r1=z['results']

r2=r1[0]
print (r2)

r3=r2['now']

print (r3)

r4=r3['clouds']

print (r4)

r5=(((z['results'])[0])['now'])['clouds']
print (r5)