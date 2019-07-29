# -*- coding: utf-8 -*-
#version 1.8

class createpassword:
	def __init__(self,file_name,add_name,save_name):
		self.file_name=file_name
		self.add_name=add_name
		self.save_name=save_name


	def add_process(self):
		z=self.add_name.title()
		b1=('',self.add_name)
		b2=(self.add_name,'')
		b3=(z,'')
		b4=('',z)
		return (b1)
		return (b2)
		return (b3)
		return (b4)

	def file_process(self):
		sea=[]
		with open(self.file_name) as f:
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
	def save_process(self,n1):
		with open(self.save_name,'w+') as s:
			s.writelines(n1)
			s.writelines('\n')
			s.close()





		# for i in (b1,b2,b3,b4):
		# 	y=file_line.join(i)	
		# 	x=y.upper()
		# 	w=y.title()







	# if __name__=="__main__":
	# 	# createpassword.file_process(self)
	# 	add_process()
		# result1=createpassword.file_process()
		# print ('abc')








# 	def line_process(file_line,add_name):
# 		z=add_name.title()
# 		b1=('',add_name)
# 		b2=(add_name,'')
# 		b3=(z,'')
# 		b4=('',z)
# 		d1=file_line.upper()
# 		d2=file_line.title()

# 		for i in (b1,b2,b3,b4):
# 			y=file_line.join(i)	
# 			x=y.upper()
# 			w=y.title()
# 		'''
# 		需要写入文件的变量 d1 d2 y x w 

# 		'''

# class done:
# 	def file_process(file_name):
# 		sea=[]
# 		with open(file_name) as f:
# 			while True:
# 				line = f.readline()
# 				if line:					#如果line不等于整型0 int
# 					line=line.strip('\n')
# 					sea.append(line)
# 					# print (line)
# 				else:
# 					break
# 			f.close()
# 		return	(sea)




# a7=createpassword('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','eae','C:\\Users\\lilei8\\Desktop\\password\\no.1\\resultttt.txt')
# a10=a7.main()
# a9=a7.save_process()
# a8=a7.file_process()
# print (a8)
# a5=createpassword.file_process('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt')
# print (a5)