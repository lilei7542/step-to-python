a=[1,3,5,7]
b=[2,4,6,8]
c=[11,12,13]
d=[11,21,31]
# e={[2,3]:2,[4,5]:3}  #no，type list no permit
e={2:3,3:4}
f={4:5,5:6}
# g={e:10,f:20}  #no ,tpye dict no permit 

a=int(input('please input a year '))
if (a%4)==0:
	if (a%100)!=0:
		print (a ,"is 闰年")
	else:
		print (a ,"is not 闰年")
else:
	print (a ,"is not 闰年")

