#for use file 
# 操作系统的编码，windows为gbk，linux为utf－8

# 打开文件的模式有：

# r ，只读模式【默认模式，文件必须存在，不存在则抛出异常】
# w，只写模式【不可读；不存在则创建；存在则清空内容】
# x， 只写模式【不可读；不存在则创建，存在则报错】
# a， 追加模式【可读； 不存在则创建；存在则只追加内容】
# “+” 表示可以同时读写某个文件

# r+， 读写【可读，可写】
# w+，写读【可读，可写】
# x+ ，写读【可读，可写】
# a+， 写读【可读，可写】
# “b”表示以字节的方式操作

# rb 或 r+b
# wb 或 w+b
# xb 或 w+b
# ab 或 a+b
# 注：以b方式打开时，读取到的内容是字节类型，写入时也需要提供字节类型，不能指定编码




file1 = open('D:\\python_project\\file_process\\f_a_1.py','a+')
file1.write('i am a champian')
# print (file1.seek(2,0))
# print(file1.read())
file1.close()

# file1 = open('D:\\python_project\\file_process\\f_a_1.py','r')
# print(file1.read())
# file1.close()
# print (dir(file1))



# with所求值的对象必须有一个__enter__()方法，一个__exit__()方法

# not ok 
# from  datetime import *
# with datetime.now() as p:
# 	a=p.month



with open('D:\\python_project\\file_process\\f_a_1.py','a+') as file1_add,open('D:\\python_project\\file_process\\f_a_1.py','r') as file1_r:
	file1_add.write('i a happy now')
	print (file1_r.read())
	file1_add.close()
	print (file1_r.read(3))
	file1_r.close()           #自己关自己的


#this is show startwith
a='abc'
if a.startswith	('a1'):
	print ('true')
else:
	print ('flase')

# import os
# os.getcwd()                ：       得到当前的工作目录
# os.listdir()                   ：       返回制定目录下的所有文件和目录名
# os.path.dirpath()         ：       获取路径名称
# os.path.abspath()       ：      获取绝对路径
# os.path.basename()   ：      获取当前的文件名称
# os.replace(old，new) ：      将文件重命名 
# os.listdir()                   ：       返回制定目录下的所有文件和目录名
# os.path.dirpath()         ：       获取路径名称
# os.path.join(path,name) ：   将名称为name的字符串与path路径拼接
# os.path.getsize(filename)    : 获取文件的大小
# os.path.split()             :           返回一个文件的目录名和文件名
# os.rename()
# os.remove()


