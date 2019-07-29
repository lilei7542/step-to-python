import requests


url='http://www.weather.com.cn/data/sk/101051301.html'

a=requests.get(url)

a.encoding='utf-8'

a1=a.json()

# print (type(a1))
print (a1)

print ('-----------')

print ('city:',(a1['weatherinfo'])['city'])
print ('temp:',(a1['weatherinfo'])['temp'])