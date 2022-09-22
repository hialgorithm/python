print("--------类的特殊属性------")
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
class E(B):
    pass
stu=C('张三',20)
print(stu.__dict__)  #类以字典的形式输出  实例对象的属性字典

print(C.__dict__)  #类对象的属性字典
print(stu.__class__)  #输出实例属性的类
print(C.__bases__)  #输出所有上一级父类
print(C.__base__)  #输出位于第一个的父类
print(C.mro()) #输出其所有的父类及其自己的类型
print(A.mro())
print(A.__subclasses__()) #输出其所有的子类
print(B.__subclasses__())
print("--------------------------------------")
a=10
b=20
c=a+b
d=a.__add__(b)
print(c)
print(d)

class Add:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Add('jack')
stu2=Add("李四")

s=stu1+stu2#字符不能直接相加  需要在类中使用__add__ 方法
print(s)
s1=stu1.__add__(stu2)
print(s1)
print("-------------------------")
se=[11,22,33,44]
print(len(se))#len 求数组的长度
print(se.__len__())#求长度
print(len(stu1))
print(stu1.__len__()) #求字符长度
print(stu2.__len__())
print("----------__new__与__init__的使用--------------")
class Person():
    def __new__(cls, *args, **kwargs):
        print('cls的地址{0}'.format(cls))
        obj=super().__new__(cls)
        print('__init__被调用，obj的地址{0}'.format(id(obj)))
        return obj

    def __init__(self,name,age):
        print('__init__被调用,self的id值为:{0}'.format(id(self)))
        self.name=name
        self.age=age

print('object这个类对象的ID为:{0}'.format(id(object)))
print("Person这个类对象的id为{0}".format(id(Person)))
p1=Person("张三",20)
print('p1这个Person类的实例对象为:{0}'.format(id(p1)))

print("---------------------")
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk
cpu1=CPU()
cpu2=cpu1
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))
print("----------------")
disk=Disk()
computer=Computer(cpu1,disk)
import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)
print("--------------")
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)