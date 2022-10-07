"""
#获取当前时间
import time
import datetime
x=datetime.datetime.now()
s=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print(x)
print(s)
print(x.year)
print(x.day)
#计算两个日期之间的天数
import time
import datetime
def t():
    a = input('请输入日期如20000819')
    b = input('请输入日期如20000819')
    a = a.strip()
    b=b.strip()
    a1=a[0:4]+'-'+a[4:6]+'-'+a[6:8]
    b1 = b[0:4] +'-'+ b[4:6] +'-'+ b[6:8]
    s=datetime.datetime.strptime(a1,'%Y-%m-%d')
    s1 = datetime.datetime.strptime(b1, '%Y-%m-%d')
    s2=s-s1
    return s2
print(t())

import datetime
day1=input('请输入日期如1222-12-12')
day1_1=datetime.datetime.strptime(day1,'%Y-%m-%d')
day2=input('请输入日期如1222-12-12')
day2_1=datetime.datetime.strptime(day2,'%Y-%m-%d')
s=day1_1-day2_1
print(s)
"""
