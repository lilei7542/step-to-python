# no.1   定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域

a=100
def show_f_l(a,b):
	a=a+b
	print (a)
	return a
show_f_l(5,8)
print (a)


# no.2使用嵌套循环输出2~100之间的素数




