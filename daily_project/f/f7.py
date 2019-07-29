from bs4 import BeautifulSoup
import json
soup=BeautifulSoup(open('D:\\python_project\\see.html'),'html.parser')

# print (soup.prettify())
# print (soup.title())
# print (soup.head())
# print (soup.a)
# print (soup.a.next_sibling)
# print (soup.a.name)
# print (soup.a.attrs)
# print ('----------')

# for we in (soup.a.next_siblings):
# 	print (we)


r1=soup.find_all('a')
# print (r1)
r1_1=json.loads(r1)
r2=soup.find_all('td')
# print (r2)

with open ('D:\\python_project\\result\\a1','w+') as f1:
	f1.readlines(json.dumps(r1))
	f1.close()