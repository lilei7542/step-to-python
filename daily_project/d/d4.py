import turtle
turtle.title('数据驱动的动态路径绘制')
turtle.setup(1200,600,0,0)

#设置画笔
pen = turtle.Turtle()
pen.color("red")
pen.width(5)
pen.shape("turtle")
pen.speed(5)

#read the file to the list result

# file=open("D:\\python_project\\file_process\\f_a_2.py","w")
# file.close()

result=[]
file=open("D:\\python_project\\file_process\\f_a_2.py","r")
for line in file:
    result.append(list(map(float,line.split(','))))
print (result)

#根据每一条数据记录进行绘制

for i in range(len(result)):
    pen.color((result[i][3],result[i][4],result[i][5]))
    pen.fd(result[i][0])
    if result[i][1]:
        pen.rt(result[i][2])
    else:
        pen.lt(result[i][2])