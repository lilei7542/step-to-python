# no.1
i = 0  
while i < 10 :  
      
    i = i + 1   
    if i == 4:  
#     #     pass  
#     # # if i == 6:  
#     # #     continue  
#     if i == 8:  
      break 

print(i)  
# else:  
#     print ('It is over.')


# no.2
a=10
b=4

# c=a%b
# if a>2:
# 	print (c)
# else: 
# 	print (b)


while b<a:
	b+=1
	print (b)
	# pass
	# continue
	break
print ("------------")
print (a)

# no.3
# python 中，while … else 在循环条件为 false 时执行 else 语句块
def jkl(count):
	# count = 0
	while count < 5:
	   print (count, " is  less than 5")
	   count = count + 1
	else:
	   print (count, " is not less than 5")
	return
jkl(3)   