"""def triangle(a,b,c):
    if a<0 or b<0 or c<0:
        raise Exception('三角形边长不能为负数')
    elif a+b<=c or a+c<=b or b+c<=a:
        raise Exception('三角形两边之和需大于第三边')
    else:
        print('三角形三边长为:',a,b,c)
if __name__ == '__main__':
    try:
        a=int(input('请输入数字'))
        b=int(input('请输入数字'))
        c=int(input('请输入数字'))
        triangle(a,b,c)
    except ValueError as f:
        print(f)
圆的面积及周长
import math
class Circle:
    def __init__(self,r):
        self.r=r

    def area(self):
        return math.pi*pow(r,2)
    def s(self):
        return 2*math.pi*r

if __name__ == '__main__':
    r=int(input('请输入半径'))
    print('周长为',Circle.s(r))
    print('面积为',Circle.area(r))

    print(f'周长为{Circle.s(r):.2f}')
    print(f'周长为{Circle.area(r):.2f}')
"""
class Student:
    def __init__(self,name,age,sex,grade):
        self.name=name
        self.age=age
        self.sex=sex
        self.grade=grade
    def s(self):
        print(self.name,self.age,self.sex,self.grade)

if __name__ == '__main__':
    lst=[]
    for i in range(0,5):
        info=input(f'请输入第{i+1}为信息(例:姓名#年龄#性别#成绩#)')
        ls=info.split('#')
        l=Student(ls[0],ls[1],ls[2],ls[3])
        lst.append(l)
    for item in lst:
        item.s()















