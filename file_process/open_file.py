wo= open('D:\\python_project\\module_myown\\file_for_use.py', 'r+')
#合法的mode有：
# r、rb、r+、rb+、w、wb、w+、wb+、a、ab、a+、ab+
# r+ 就是 rw 

# print (dir(wo))


# wo.write('a good test fffffffffffffffffff')
# a=('a','b','c','d','e','f','g','h')
# for b in a:

# b=wo.readline()
# print (b)
	# wo.writelines('\r\n')
	# wo.writelines(b)


# a=wo.seek(1)
# wo.write('abcd')

# p=wo.tell()
# print(p)
# print (type(wo.close))
# print (type(wo.close()))
# i=3
# i=100
for i in wo:
	# print (dir(i))
	wo.writelines('b')
	wo.writelines('\r\n')
	


wo.close()


