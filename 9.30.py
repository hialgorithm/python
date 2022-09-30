"""phone=set()
for i in range(0,5):
    a=input('请输入需要添加的信息')
    phone.add(a)
#print(phone)
for item in phone:
    print(item,end=' ')

c='hellopython,Hellojava,hellojango'
ch=input('请输入你需要查找的字母')
count=0
for item in c:
    if item.upper()==ch or item.lower()==ch:
        count+=1
print(count)


def g_count(c,ch):
    count = 0
    for item in c:
        if item.lower()==ch or item.upper()==ch:
            count+=1
    return count
if __name__ == '__main__':
    c = 'hellopython,Hellojava,hellojango'
    ch = input('请输入你需要查找的字母')
    counts=g_count(c,ch)
    print(f'{ch}在{c}中的个数为{counts}')

def show():
    print('编号', '\t''名称', '\t''品牌', '价格')
    for item in lst:
        for i in item:
            print(i, end='\t')
        print()
lst=[['01','电风扇','美的',500],
     ['02','洗衣机','TCL',1000],
     ['03','微波炉','老板',400]]

show()

print('---------------')
for item in lst:
    item[0]='0000'+item[0]
    item[3]='¥{:.2f}'.format(item[3])
show()

def fun(a,b):
    c=a+b
    print(c)
s1=fun(10,20)

def fun(a,b,op):
    if op=='+':
        return add(a,b)
    elif op=='-':
        return sub(a,b)
    elif op=='*':
        return mul(a,b)
    elif op=='/':
        if b!=0:
            return div(a,b)
        else:
            print('除数不能为0')
def add(a,b):
    return a+b
def sub(a,b):
    return  a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
if __name__ == '__main__':
    a=int(input('请输入一个数字'))
    b=int(input('请输入另一个数字'))
    op=input('请输入操作符')
    print(fun(a,b,op))
   """
"""
错误代码
import random
num=random.randint(1,100)
def fun(a):
    for _ in range(0,10):
        if num<a:
            print('大了')

        elif num>a:
            print('小了')

        else:
            print('恭喜你，猜对了')

a=int(input('我心里有个数，请你猜一猜:'))
fun(a)

import random
def fun(guess,num):
    if guess==num:
        return 1
    elif guess<=num:
        return 0
    else:
        return -1
num=random.randint(1,100)
for i in range(0,10):
    guess=int(input('请输入数字'))
    x=fun(guess,num)
    if x==1:
        print('猜对了')
        break
    elif x==0:
        print('小了')
    elif x==-1:
        print('大了')
else:
    print('次数用完')

x=int(input('请输入数字'))
if 0<=x<=100:
    print(x)
else:
    raise Exception('超出范围')

x=int(input('请输入数字'))
try:
    if 0<=x<=100:
        print(x)
    else:
        raise Exception('超出范围')
except Exception as c:
    print(c)
"""
try:
    x=int(input('请输入数字'))
    if 0 <= x <= 100:
        print(x)
except  ValueError as e:
    print(e)