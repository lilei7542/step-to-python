# -*- coding: utf-8 -*-
#version 1.2

word = 'normaster'
# word_seq= ('','normaster')
word_seq1= ('',word)
word_seq2= (word,'')
t=[]
with open ('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','r') as f, open ('C:\\Users\\lilei8\\Desktop\\password\\no.1\\result.txt','w+') as s:
	for line in f.readlines():
	    line1=line.strip('\n')
	    t.append(line1)
	for t1 in t:
		m1=str(t1)
		m2=m1.join(word_seq1)
		m3=m1.join(word_seq2)
		s.writelines(m1)
		s.writelines('\n')
		s.writelines(m2)
		s.writelines('\n')
		s.writelines(m3)
		s.writelines('\n')
	f.close()
	s.close()