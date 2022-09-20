"""print("---------程序调试-----------")
i=1
while i<10:
    i+=1
    print(i)


class Sb:
    native_pace="安徽" #类属性
    def __init__(self,name,age):#初始化方法
        self.name=name
        self.age=age
    #实列方法
    def eat(self):
        print("在吃东西")
    #静态方法
    @staticmethod
    def drink():
        print("在喝茶")
    #类方法
    @classmethod
    def sex(cls):
        sexs="男"
        print(sexs)
stu1=Sb("张三",20)
stu1.eat()#对象名.方法名
stu1.drink()
stu1.sex()
print('---------------')
print(stu1.name)
print(stu1.age)
print('---------------')
Sb.eat(stu1) #类名.方法名
Sb.sex()
Sb.drink()
#print(id(Sb))
#print(type(Sb))
#print(stu1)
print("-------------")
print(Sb.native_pace)
print(stu1.native_pace) #类属性对所有对象通用
stu2=Sb('王二麻子','28')
print(stu2.native_pace)
print("---------类方法----------")
Sb.sex()
print("----------静态方法----------")
Sb.drink()
"""

class Student:
    place="安徽"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')
    @staticmethod
    def drink():
        print('在喝茶')

stu1=Student("张三",20)
stu2=Student("李四",30)
stu1.eat()
stu2.drink()
stu2.sex='男' #动态绑定
print(stu2.name,stu2.age,stu2.sex)
print(stu1.name,stu1.age)

def fun():
    print('定义在外部的函数')

stu1.fun=fun #函数的动态绑定
stu1.fun()
print(stu1.fun,stu1.name)

name="张三"
def f1():
    print(name)
def f2():
    name="李四"
f1()
f1()
f2()

