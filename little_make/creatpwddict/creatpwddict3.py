# -*- coding: utf-8 -*-
#version 1.3

# import re
# def titlecase(s):
#      return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(),s)



word = 'normster'
t_word_seq=word.title()
word_seq1= ('',word)
word_seq2= (word,'')
t_word_seq1=('',t_word_seq)
t_word_seq2=(t_word_seq,'')
t=[]
with open ('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','r') as f, open ('C:\\Users\\lilei8\\Desktop\\password\\no.1\\result.txt','w+') as s:
	for line in f.readlines():
	    line1=line.strip('\n')
	    t.append(line1)
	for t1 in t:
		m1=str(t1)
		m2=m1.join(word_seq1)
		m3=m1.join(word_seq2)
		m4=m1.upper()
		m5=m1.title()
		s.writelines(m1)
		s.writelines('\n')
		s.writelines(m2)
		s.writelines('\n')
		s.writelines(m3)
		s.writelines('\n')
		s.writelines(m4)
		s.writelines('\n')
		s.writelines(m5)
		s.writelines('\n')
	for t1 in t:
		n1=str(t1)
		n2=n1.join(t_word_seq1)
		n3=n1.join(t_word_seq2)
		n4=n1.upper()
		n5=n1.title()
		s.writelines(n1)
		s.writelines('\n')
		s.writelines(n2)
		s.writelines('\n')
		s.writelines(n3)
		s.writelines('\n')
		s.writelines(n4)
		s.writelines('\n')
		s.writelines(n5)
		s.writelines('\n')
		s.writelines('\n')

	f.close()
	s.close()


# 添加去除重复项功能
