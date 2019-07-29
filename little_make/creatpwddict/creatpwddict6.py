# -*- coding: utf-8 -*-
#version 1.6


# 理解self


class createpassword:
	def __init__(cde,fn,an):
		cde.file_name=fn
		cde.add_name=an
		# cde._add_name=an
		# cde.__add_name=an
		# cde._add_name=an      #私有属性
		'''

　　　　1）：单下划线_开头：只是告诉别人这是私有属性，外部依然可以访问更改

　　　　2）：双下划线__开头：外部不可通过instancename.propertyname来访问或者更改

　　　　　　实际将其转化为了_classname__propertyname
		'''
	@staticmethod
	def io():
		op='3'
		return (op)

	def file_process(cde):
		a='3'
		# print ('abc')
		with open(cde.file_name) as f:
			while True:
				line = f.readline()
				if line:					#如果line不等于整型0 int
					line=line.strip('\n')

					# print (line)
				else:
					break

			f.close()

	# def line_process(file_line,add_name):
	# 	z=add_name.title()
	# 	b1=('',add_name)
	# 	b2=(add_name,'')
	# 	b3=(z,'')
	# 	b4=('',z)
	# 	d1=file_line.upper()
	# 	d2=file_line.title()

	# 	for i in (b1,b2,b3,b4):
	# 		y=file_line.join(i)	
	# 		x=y.upper()
	# 		w=y.title()
	def g(cde):
		print (createpassword.file_process().a)
		# createpassword.file_process.a
		# print (c)




# if __name__=='__main__':
# 	j=createpassword('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','abc')
'''
将会最终执行的
'''

# createpassword('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','abc').file_process()
j=createpassword('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','abc')
j.file_process()
print (createpassword.io())
print (j.io())

# j.line_process()
# j.file_process().add_name
# print (createpassword('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','abc').add_name)
print(j.add_name)		#可以调用
# print(j._add_name)		#可以调用
# print(j.__add_name) 	#不可以调用


class A(object):  
        def kkk(cde,x):    #实例方法，类和实例都能访问  
            print(cde,x)  
        @classmethod    #加上这句后 classKkk就成为了类方法，类和实例都可以访问，  
        def classKkk(cls,x):  
            print(cls,x)  
        @staticmethod   #加上这句就成为了静态方法，类和实例都可以访问。  
        def staticKkk(x):  
            print(x)  
        def mmm(x):     # 这是无敌普通函数  
            print(x)  
A.classKkk(2)  
#   <class '__main__.A'> 2 这里类A可以直接访问类方法classKkk，但是不能访问实例方法kkk（会报错的）。  
A.kkk(A,1)  #<class '__main__.A'> 1 类要访问实例方法需要加入参数,至于这个参数可以是A也可以是A()  
A.staticKkk(3)  #   3 这里类A也可以访问静态方法staticKkk，  
A.mmm(3) #  3 对象可以访问无敌普通函数  
a = A()  
a.kkk(5)    # <__main__.A object at 0x0000028A64394CC0> 5 实例访问实例方法，没毛病  
a.classKkk(6)   #   <class '__main__.A'> 6 实例访问类方法，没毛病  
a.staticKkk(7)  #   7  
# a.mmm(7)    # 报错，实例不能访问普通函数  
  
 
    #总结：实例方法和类方法一定要传入参数，a.kkk(x)相当于kkk(a,x)，第一个参数必须是实例本身。类方法也是如此，但是静态方法不用传入参数，此外普通函数只有类能访问，对象不能访问  

