import datetime
"""
法1
def fun():
    s=input('请输入日期如20000101')
    s=s.strip()
    s1=s[0:4]+'-'+s[4:6]+'-'+s[6:8]
    s2=datetime.datetime.strptime(s1,"%Y-%m-%d")
    s3=s2-datetime.timedelta(7)
    return s3
print(fun())
法2
def fun(day,day1):
    day2=day-day1
    return day2
day=input('请输入日期')
day_1=datetime.datetime.strptime(day,'%Y-%m-%d')
day2=datetime.timedelta(7)
a=fun(day_1,day2)
print(a)
法三
def fun(day,day1):
    day_1 = datetime.datetime.strptime(day, '%Y-%m-%d')
    day1 = datetime.timedelta(days=day1)
    day2=day_1-day1
    return day2
day = input('请输入日期')
print(fun(day,9))
"""



