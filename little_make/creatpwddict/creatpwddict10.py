# -*- coding: utf-8 -*-
#version 2.1

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
		return b1,b2,b3,b4

	def file_process(self):
		sea=[]
		with open(self.file_name) as f:
			while True:
				line = f.readline()
				if line:					#如果line不等于整型0 int
					line=line.strip('\n')
					sea.append(line)
				else:
					break
			f.close()
		return	sea

	def save_process(self,n1):
		with open(self.save_name,'w+') as s:
			for u in n1:
				s.writelines(u)
				s.writelines('\n')
			s.close()	

			# if n1 is not None:
			# 	s.writelines(n1)
			# 	s.writelines('\n')
			# else:
			# 	s.close()

	def main(self):
		k1=self.add_process()
		g1=self.file_process()
		p=[]
		for t1 in g1:
			for i in k1:
				y=t1.join(i)	
				x=y.upper()
				w=y.title()
				for v in y,x,w:
					p.append(v)

		self.save_process(p)



a7=createpassword('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','eae','C:\\Users\\lilei8\\Desktop\\password\\no.1\\resultttt.txt')
a10=a7.main()

