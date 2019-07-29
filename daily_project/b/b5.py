class Animal(object):
    def run(self):
        print ('Animal is running...')

class Dog(Animal):
	def wangwang(self):
		print('a scream')
	print("hah")
    # pass

class Cat(Animal):
    pass



# a=Dog()
# a.run()

c=Dog()
# print (c.wangwang())
c.wangwang()



# %d	整数                %f	浮点数               %s	字符串                   %x	十六进制整数
print('Hi, %s, you have $%s.' % ('Michael', '1000000'))
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print (u'中午')




class Person():
    name = "zhengtong"

if __name__ == "__main__":
    x = Person()


Person()
print(x.__class__) #定位类
print(x.name) #定位类
print(dir(x))
print(type(x))