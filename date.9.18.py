"""def s(a,b):#形参
    c=a*b
    return c
d=s(10,20)#实参
print(d)

result=s(b=5,a=7)#实参
print(result)

def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(100)
    print('arg1',arg1)
    print('arg2',arg2)


a=10 #a是不可变数据
b=[10,20,30] #b是可变数据
print('a',a)
print('b',b)
fun(a,b)
print('a',a)
print('b',b)

print("------不用return的情况--------")
def fun():
    print('hello')

fun()

print("-------return一个参数----")
def fun1():
    return 'hello'

res=fun1()
print(res)
print("--------retun多个参数-------")
def fun2():
    return 'hello','world'

res1=fun2()
print(res1)
print("-------实际操作-------")
def fun3(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

s=[1,3,4,6,7,8,9,0]
res5=fun3(s)
print(res5)

def fun4(a,b=10):
    return a,b

res6=fun4(100)
print(res6)
res7=fun4(100,20)# 若函数fun中有两个数据，调用时只使用1个参数，则前面的参数被改变，后面的参数保持不变（即默认值）。若赋予的值必形参的数量多，则报错
print(res7)

def fun5(a=20,b=30):
    print(a,b)

fun5(50)
fun5(60,70)

def fun(*s):#个数可变的位置参数，且一个函数中只可以存在一个
    print(s)

fun(10)
fun(10,20)
fun(10,67,87)

def fun1(**c):#个数可变的关键字参数，且一个函数中只可以存在一个
    print(c)

fun1(a=10,b=20)

def fun2(*b,**d):
    print(b,d)

fun2(10,20,a=20)

def fun3(**e,*f):#若位置参数与关键字参数同时存在，位置参数必须在关键字参数前面
    print(e,f)
fun(a=20,30)

def fun(a,b):
    print(a,b)

x=10
x1=10
lst=[1,2]
fun(x,x1)
fun(*lst)#如果函数调用集合或者裂表等，且形参的数量多于实参的数量，则实参前面需要添加“*”

def fun1(a,b,c):
    print(a,b,c)

fun1(a=10,b=20,c=30)
lst1={'a':11,'b':22,'c':33}
fun1(**lst1)

def fun(a,b):
    c=a+b
    print(c)

#print(a) #参数在函数体内部，为局部参数

s='张三'
print(s)

def fun2():
    print(s)
#其中“张三”为外部变量
fun2()

def fun3():
    global age
    age=20#局部变量改为全局变量需要使用globle声明
    print(age)
fun3()
print(age)


print("-------递归--------")
def fun(n):
    if n==1:
        return 1
    else:
        a=n*fun(n-1)
        return a

print(fun(10))
"""
print("-------斐波那契数---")
def fun(n):
    if n<=2:
        return 1
    else:
        a=fun(n-1)+fun(n-2)
        return a
print(fun(9))
print("---------------")
for i in range(1,10):
    print(fun(i))



