class Person(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

class Child(Person):                          # Child 继承 Person
    def __init__(self,name,sex,mother,father):
        Person.__init__(self,name,sex)        # 子类对父类的构造方法的调用
        self.mother = mother
        self.father = father

May = Child("May","female","April","June")
print(May.name,May.sex,May.mother,May.father)


class Person(object):
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
        
    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("woman")
            
class Child(Person):
    pass

class Baby(Child):
    pass

May = Baby("May","female")        # 继承上上层父类的属性
print(May.name,May.sex)            
May.print_title()                 # 可使用上上层父类的方法


class Child(Person):                
    def print_title(self):
        if self.sex == "male":
            print("boy")
        elif self.sex == "female":
            print("girl")
            
class Baby(Child):
    pass
            
May = Baby("May","female")
print(type(May))
May.print_title()                # 优先使用上层类的方法