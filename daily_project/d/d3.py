f=open("D:\\python_project\\file_process\\aaa.txt","w")     #以只写的形式打开一个叫做aaa.txt的文件
f.write("my name is liuxiang,i am come frome china")   #写入内容
f.close()     #关闭文件
f=open("D:\\python_project\\file_process\\aaa.txt","r")     #以只读打开文件
f.read()   #读取内容
'my name is liuxiang,i am come frome china'      
f.seek(3,0)      #“0”代表从文件开头开始偏移，偏移3个单位
f.read(5)     #从偏移之后的指针所指的位置（即“n”）开始读取5个字符
'name '
>>> f.tell()     #显示现在指针指在哪个位置（即“i”的位置）
>>> f.readline()       #读取这一行剩下的内容
'is liuxiang,i am come frome china'     



>>> f.seek(0,2)      #“2”代表从末尾算起，“0”代表偏移0个单位
>>> f.read()
''         #因为是从末尾算起，内容已结束。所以读取内容为空