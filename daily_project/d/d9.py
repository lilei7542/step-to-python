# match = re.search(pattern, string)
# if match:
#     process(match)

import re
 
print(re.search('www', 'www.runoob.com'))  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())





we=re.match('world',"worldcup")
a=we.span()
b=we.group()
print(a)
print(b)



import os
print(os.getcwd())