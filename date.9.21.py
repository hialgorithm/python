class Student:
    def __init__(self,name,age,sex):
        self.name=name
        self.__age=age #若不想被外部调用可使用”__“
        self.sex=sex
    def brand(self):
        print(self.name)
        print(self.__age)
        print(self.sex)

stu=Student("张三",25,'男')
stu.brand()
print(stu.sex)
#print(stu.age)#表示不可被外部调用成功
print("如果想对其进行外部调用")
print(dir(stu))
print(stu._Student__age) #强行调用的方法

print("-----------类对象的外部调用----------")
class Car:
    def __init__(self,name):
        self.name=name
    def s(self):
        print('启动')

car=Car("奔驰s")
car.s()
print(car.name)

print("-------------继承及实现方式-------------")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def infomation(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age) #()内部必须添加元素
        self.id=id
class Teacher(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year=year
student1=Student("张三",20,2010902)
teacher=Teacher("李四",45,12)
student1.infomation()
teacher.infomation()
print("-------多个继承---------")
class C:
    pass
class B:
    pass
class Su(C,B):
     pass

print("------方法重写------")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def infomation(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,id):
        super().__init__(name,age) #()内部必须添加元素
        self.id=id
    def infomation(self):
        super().infomation()
        print(self.id)
class Teacher(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year=year
    def infomation(self):  #如果需要在父类中添加不一样的元素，调用时使用的函数需要与父类相等
        super().infomation()
        print(self.year)
student1=Student("张三",20,'2010902')
teacher=Teacher("李四",45,12)
student1.infomation()
teacher.infomation()

print("--------多态--------")
class Fun():
    def eat(self):
        print("吃东西")
class Dog(Fun):
    def eat(self):
        print("狗吃骨头")
class Cat(Fun):
    def eat(self):
        print("猫吃鱼")
class Person():
    def eat(self):
        print("人吃五谷杂粮")

def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Person())
