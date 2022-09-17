"""x="hello,hello,world"
print(x.index('lo'))
print(x.rindex('lo'))
print(x.find("lo"))
print(x.rfind('lo'))
#print(x.index('v')) 如果没有找到 则报错
#print(x.rindex('m'))如果没有找到 则报错
print(x.find('p'))#如果没有找到 则显示-1
print(x.rfind('u'))#如果没有找到 则显示-1

s="HELLO,world"
a=s.upper() #所有字母改成大写
print(a,id(a))
print(s,id(s))
a1=s.lower()
print(a1,id(a1)) #所有字母改成小写
a2=s.swapcase()#所有大写字母改成小写，小写字母改大写
print(a2,id(a2))
a3=s.capitalize()#第一个字母转为大写，其余字母转为小写
print(a3,id(a3))
a4=s.title()#每个单词的首字母转为大写，其余为小写
print(a4,id(a4))

b="zhangle"
print(b.center(10,"-"))
print(b.ljust(12,'-'))
print(b.rjust(15,'*'))
print(b.center(5))
print(b.zfill(15))
print("-678".zfill(8))

#字符串的劈分
c="hello,world,python"
c1="hellooworldopython"
print(c.split())
print(c1.split(sep='o'))
print(c1.split())#如果split无输入值，则默认以‘ ’作为分隔标志
print(c.rsplit())
print(c1.rsplit(sep='o',maxsplit=1))

#字符串的判断
l="hello,"
print(l.isidentifier())#","不是常用标识符
print('hello'.isidentifier())
print('he12_'.isidentifier())
print('\t'.isspace())
print('kjgfds四'.isalpha())#判断是否全部由字母组成
print('546'.isdecimal())#判断是否由十进制数字组成
print("87四".isnumeric())#判断是否由数字组成
print("9879sdf".isalnum())#判断是否由数字及字母组成
print('890fgdg..'.isalnum())

print(l.replace('o','t'))
print('hello.world'.replace('world','hello'))
f='hello,python,python,python'
print(f.replace('python','java',1))#如果替换时，有n个重复且未指定替换多少个，则全部替换
print(''.join(f))
print('*'.join(f))
print('!'.join(f))
g=['dfg','hello']
print(''.join(g))
print('!'.join(g))

print('apple'>'pine')
print(ord('a'),ord('p'))
print(ord("张"),ord("高"))
print(chr(24352),chr(39640))
print('a'=='ap')
print('a'=='a')
print('a' is 'a')
"""
print("------字符串的增删改------")
s="hello,world"
s1=s[:4:1]
s2=s[6::1]
s3='!'
new=s1+s3+s2
print(s1)
print(s2)
print(new)

s4=s[1:6:2]
s5=s[5:10:3]
print(s4)
print(s5)

s8=s.__add__('i')
print(s8)

name="张三"
age=20
print("我叫%s,我今年%d岁" % (name,age))
print("我叫{}，我今年{}岁".format(name,age))
print("我叫{0}，我今年{1}岁".format(name,age))
print(f"我叫{name}，我今年{age}岁")
print("%10d" % 90)#一个占10个字符（其中包括90这两个字符）
print("hellohello")
print("%.3f" % 3.1415926)#保留三位小数
print("%10.3f" % 3.1415)#占十个字符，数据保留三位小数
print("{:.3}".format(3.1415926))#一共保留三位数
print("{:15.3}".format(3.1415))
print("{:.3f}".format(3.1415926))#保留三位小数


c="张乐"
#print(c.encode(encoding='GBK'))
byte=c.encode(encoding='GBK')
print(byte.decode(encoding="GBK"))

d="天涯共此时"
byte=d.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

