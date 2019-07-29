# -*- coding: utf-8 -*-
#version 1.4

class change:

	def line_process(file_line,add_name):
		z=add_name.title()
		b1=('',add_name)
		b2=(add_name,'')
		b3=(z,'')
		b4=('',z)
		d1=file_line.upper()
		d2=file_line.title()

		for i in (b1,b2,b3,b4):
			y=file_line.join(i)	
			x=y.upper()
			w=y.title()
		'''
		需要写入文件的变量 d1 d2 y x w 

		'''

class done:
	def file_process(file_name):
		with open(file_name) as f:
			while True:
				line = f.readline()
				if line:					#如果line不等于整型0 int
					line=line.strip('\n')
					return (line)
					# print (line)
				else:
					break
			f.close()







# print (type(done.file_process('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt').line))
# print (type(done.file_process('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt')))
# done.file_process(file_name).line
# done.file_process().line
#都不行，不对


def k():
	c='a'

r=k()
print (dir(r))
print (type(r))
