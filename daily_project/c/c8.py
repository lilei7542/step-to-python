z = ["a", "b", "mpilgrim", "z", "example"]
print (z)
z.append('jack')
print (z)
print (z[2])
z.pop()
z.pop(1)
print (z)
print (z[-1])
print (z)
z.insert(3,'suse')
print (z)
z.extend(['fd','ftp'])
print (z)
x=z.index('fd')
print (x)
z=z+['dududu']+['lalala']
print (z)
print('----------------------------------------')
print('----------------------------------------')

for i in range(5):
	# h=str(z[-1])
	i=1
	i+=1
	h=str(z.pop(-1))
	print('my name is %s' %h)

print (z)

#       %s  传递str参数
#       %d  传递int参数
#       %f  传递float参数


print("My name is %s" %("Alfred.Xue"))
print("My year is %d" %(25))
print("My weight is %f kg" %(68.2))

name='john'
old ='20'
print("My name is %s and i'm %d" %('john', 12))
print("My name is %s and i'm %s" %(name, old))  #多个%s参数
print ('-------------------------------')


#list can change str simplely into list
tmpstr = 'abcdefg,jj'
tmplist = list(tmpstr)
print (tmplist)
print ('-------------------------------')


#how to use join 
#funtion-> translate list into str
we=",".join(tmplist)
wr="".join(tmplist)
print (we)
print (wr)
print (type(we))
print ('-------------------------------')




#in dictionary
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print (params['database'])
g=params.keys()
y=str(g)
print (type(g))
print (type(y))
print (y)
print (params.keys())
# ['server', 'uid', 'database', 'pwd']
print(params.values())
# ['mpilgrim', 'sa', 'master', 'secret']
print(params.items())
# [('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
import re
k1=re.sub(r'dict_keys','',y)
# k3=re.sub(r'uid','pid',y))
k2=re.sub(r'\'*','',k1)
k3=re.sub(r'\[','',k2)
k4=re.sub(r'\]','',k3)
k5=re.sub(r'\(','',k4)
k6=re.sub(r'\)','',k5)

print (k1)
print (k6)
# print (k3)
print ('------------------------------')


import re
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
g1=str(params.keys())
g2=re.sub(r'dict_keys','',g1)
g3=re.sub(r'[\(\)\[\]\']*','',g2)
print (g3)
print ('------------------------------')


r1=["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
#method 1
#can't 
# for t1 in r1:
# 	if len(t1)>1:
# 		t2=t1
# 		r1.remove(t2)
# 		print (r1)

# method 2
# amazing i think
for i in range(0,7):
	i=0
	i+=1
	for t1 in r1:
		if len(t1)>1:
			r1.remove(t1)
			print (r1)

print ('------------------------------')

