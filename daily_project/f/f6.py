from bs4 import BeautifulSoup
import urllib.request

url='http://www.weather.com.cn/weather/101010100.shtml'

a1=urllib.request.urlopen(url)

# print (a1.read())

b1=BeautifulSoup(a1,'lxml')

c1=b1.find('p',title="阴转多云") 

c2=b1.p

# c3=b1.p['class']

c4=b1.a

c5=b1.find_all('a')



print (c1)
print (c2)
# print (c3)	
print ('-----------------')
print (c4)
# print (c5)


for d1 in c5:
	d2=d1.get('href')
	print (d2)

print (type(c5))

