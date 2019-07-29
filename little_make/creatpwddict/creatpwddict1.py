# -*- coding: utf-8 -*-
#version 1

#for intrude a backstagesystem
# this is a start, see more

# a = 'normaster'
# a1=a.strip('nor')
# print (a1)
# seq=('1','',)
# seq2=('2','',)
# seq3=('','3')
# # print (str.join(seq))
# print (a.join(seq))
# print (a.join(seq2))



word = 'normaster'
# word_seq= ('','normaster')
word_seq= ('',word)
t=[]
with open ('C:\\Users\\lilei8\\Desktop\\password\\no.1\\200-simple.txt','r') as f, open ('C:\\Users\\lilei8\\Desktop\\password\\no.1\\result.txt','w+') as s:
	for line in f.readlines():
	    line1=line.strip('\n')
	    line2=line1.join(word_seq)
	    t.append(line2)
	for t1 in t:
		m1=str(t1)
		s.writelines(m1)
		s.writelines('\n')

	f.close()
	s.close()