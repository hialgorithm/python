import time
"""
def show_info():
    print('请输入数字，执行相对应的操作:0.退出 1.查看登录日志')

#写入日志
def w_day(usename):
    with open('log.txt','a') as file:
        s=f'用户名为{usename}，登录时间为{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        print('\n')
#读取日志
def r_day(usename):
    with open('log.txt','r') as file:

        while True:
            line = file.readline()
            if line=='':
                break
            else:
                print(line,end='')

if __name__ == '__main__':
    usename=input('请输入用户名')
    my=input('请输入密码')
    if usename=='zhangle' and my=='zl12345':
        print('登陆成功')
        w_day(usename)#登录成功之后开始写入
        show_info()#写入之后，开始进行选择
        num=int(input('请输入数字'))
        while   True:
            if num==0:
                print('退出')
                break
            elif num==1:
                print('查看日志')
                r_day(usename)
                num=int(input('请输入数字，执行相对应的操作:0.退出 1.查看登录日志'))
            else:
                print('输入错误，请重新错误')
                show_info()
                num = int(input('请输入数字，执行相对应的操作:0.退出 1.查看登录日志'))
    else:
        print('密码或用户名错误')
#两数之和
def add(a,b):
    c=a+b
    return c

a=int(input('请输入数字'))
b=int(input('请输入数字'))
c=add(a,b)
print(c)

#阶乘
def s(num):
    i=1
    while num>0:
        i*=num
        num-=1
    return i
def s(num):
    a=1
    for i in range(1,num+1):
        a*=i
    return a

num=int(input('请输入数字'))
print(s(num))
#求圆的半径
import math
r=int(input('请输入半径'))
s=math.pi*math.pow(r,2)
print(s)
#求区间素数
def prime(i):
    if i==1 or i==2:
        return i
    for inx in range(2,i):
        if i%inx==0:
            return False
    return i

for i in range(1,101):
    if prime(i):
        print(i)

#前n项平方和
import math
def add_mul(num):
    sum=0
    for i in range(1,num+1):
        sum+=math.pow(i,2)
    return sum
num=int(input('请输入数字'))
print(add_mul(num))
#计算列表中数字的和
def fun(i):
    i=0
    for item in s:
        i=i+item
    return i
s=[1,3,5,7]
print(fun(s))

#计算范围内所有的偶数
def fun(num):
    r=[]
    for i in range(1,num+1):
        if i%2==0:
            r.append(i)
    return r

num=int(input('输入数字'))
print(fun(num))
#移除列表中的元素
def f(a,b):
    for item in b:
        a.remove(item)
    return a
a=[1,2,3,4,5]
b=[2,4]
print(f(a,b))
#去除列表中重复的数据
def fun(a):
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    return x
if __name__ == '__main__':
    a=[10,30,10,20,20]
    print(f'原列表{a}，去除重复数字后{fun(a)}')

#排序
import math
import os
a=[10,30,10,20,20]
b=['b','d','c','a','r','v']
a.sort(reverse=True)#降序排序
d=sorted(b)#升序排序
c=sorted(b,reverse=True)#降序排序
print(a)
print(c)
print(d)
"""
#学生排序
student=[
            {'sno':101,'sn':'hfds','sgr':89},
            {'sno':102,'sn':'hfd','sgr':78},
            {'sno':103,'sn':'hf','sgr':88}
        ]
s=sorted(student,key=lambda x:x['sgr'])
s1=sorted(student,key=lambda x:x['sno'])
s2=sorted(student,key=lambda x:x['sn'])
print(s)
print(s1)
print(s2)