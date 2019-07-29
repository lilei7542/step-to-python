# -*- coding: utf-8 -*-
#version 1.7

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
		sea=[]
		with open(file_name) as f:
			while True:
				line = f.readline()
				if line:					#如果line不等于整型0 int
					line=line.strip('\n')
					sea.append(line)
					# print (line)
				else:
					break
			f.close()
		return	(sea)
		# print (sea)






# a5=done.file_process('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt')
# print (a5)



