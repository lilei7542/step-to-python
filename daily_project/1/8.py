# no.1  explain how to use return 
def hahaha(a,b):
	a=a+b
	# print (a)
	# return a+15
	# return b
	# return 15
	return

c=hahaha(3,5)
print(hahaha(3,5))


# no.2   每一条语句最后个加个分号；这是c,oc,java,php等语言中不可缺少的部分，
#        但是对于python,分号是可加，可不加的,建议最好还是不加分号，因为 python 是考换行来区分代码句的，当然有时候也可以加上
def printinfo( name, age = 35 ):    # 缺省参数age
   print ("Name: ", name);
   print ("Age   ", age);
   return;

printinfo( age=50, name="miki" );
printinfo( name="miki" );
print('--------------------')


# no.3

def notabsolutething(x,*y):

	for var in y:
		x=x+var
		print (x)
	return x
notabsolutething(7,8,9)
t=notabsolutething(7,8,9)    #会被执行
print (t)



# no.4
def printinfo( arg1, *vartuple ):
   # print ("输出: ")
   # print (arg1)
   # for var in vartuple:
      # print (var)
   # print (arg1)
   return arg1

a=printinfo( 10 )
b=printinfo( 70, 60, 50 )
print (a,b)



# no.5  lambda
jack=lambda tom,jeery:print ("tom love jerry")
print (jack("ice","fire"))
jack("ice","fire")
jack("ice","fire")
jack("ice","fire")
jack("i","f")
print()


