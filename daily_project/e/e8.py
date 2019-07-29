class change:

	def test1 (le):
		print('start')
		change.test2('we')

	def test2 (add_name):
		print ('jkl')
		# change.test1('a')



a=int()
change.test1(a)



class t:
	def x(a):
		print (int(a)+100)
	def y(b,a):
	# def y(b,c):
		t.x(a)
		print (b)

t.y('1','2')



class ClassA(object):

    def func_a(self):
        print('Hello Python')

if __name__ == '__main__':
    # 使用实例调用实例方法
    ca = ClassA()
    ca.func_a()
    # 如果使用类直接调用实例方法,需要显式地将实例作为参数传入
    ClassA.func_a(ca)




class Foo(object):
    """类三种方法语法形式"""

    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")

foo = Foo()
foo.instance_method()
foo.static_method()
foo.class_method()
print('----------------')
Foo.static_method()
Foo.class_method()




class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book

book1 = Book("python")
book2 = Book.create("python and django")
print(book1.title)
print(book2.title)

