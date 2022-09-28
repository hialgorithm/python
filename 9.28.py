"""
print('\033[0:35m我爱你中国\033[m')
print('\033[0:35m----------------')
print('\033[0:35mhuhuhd')
print('---------二进制----------')
num=int(input('请输入一个十进制数:'))
print(num,'十进制数为:',num)
print(num,'转换为2进制数:',bin(num))
print(num,'转换为2进制数为:'+bin(num))
print(str(num)+'转换为2进制数为:'+bin(num))
print('%s的二进制位%s:'%(num,bin(num)))#格式化字符串
print('{0}的二进制数为{1}'.format(num,bin(num)))
print(f'{num}的字符串为{bin(num)}')
print('-----------------------------------')
print(num,'转换为8进制数:',oct(num))
print(str(num)+'八进制数为:'+oct(num))
print(str(num)+'八进制数为:'+oct(num))
print(str(num)+'十六进制数为:'+hex(num))

print('--------------------------')
father=input('请输入父亲身高')
print(father)

fk=input('请输入密码:')
if fk.isdecimal():
    print('密码合法')
else:
    print('密码不合法')

if fk.isnumeric():#此方法只适合判断数字合法 不可判断符号不合法

    print('密码合法')

#print('密码合法' if fk.isdigit() else '密码不合法')

id1=input('请输入id:')
if id1=='123':
    m=input('请输入密码:')
    if m=='9999':
        print('密码正确，登陆成功')
    else:
        print('密码输入错误')
else:
    print('id输入错误')
1.
mon=int(input('请输入猜取的金额:'))
if mon==1400:
    print('恭喜你，猜对了')
elif mon<=1400:
    print('猜小了')
else:
    print('猜大了')

import random
mon=random.randint(1000,1500)
guess=int(input('请输入猜取的金额'))
if mon<guess:
    print('猜大了')
elif mon>guess:
    print('猜小了')
else:
    print('恭喜你，猜对了')
print('真实值为:',mon)

a=97
for _ in range(1,27):
    print(chr(a),a)
    a+=1

a=97
while a<123:
    print(chr(a),a)
    a+=1


for i in range(1,4):
    id1 = input('请输入姓名')
    m = input('请输入密码:')
    if id1=='123' and m=='999':
        print('登陆成功')
    else:
        if i<3:
            print(f'你还有{0}次',3-i)

水仙花数
import math
for i in range(100,1000):
    if i==math.pow((i%10),3)+math.pow((i//10)%10,3)+math.pow((i//10)//10,3):
        print(i)
        i+=1
"""
lst=[82,88,98,86,92,0,99]
print('原列表为:',lst)
for index,year in enumerate(lst):
    #print(index,year)
    if year!=0:
        lst[index]=int('19'+str(year))
    else:
        lst[index]=int('200'+str(year))
print('修改之后的列表为:',lst)
lst.sort()
print(lst)


