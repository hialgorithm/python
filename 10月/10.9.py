import datetime
"""#输出两日期之间的所有日期
def day_range(begin,end):
    lst=[]#设置空列表
    while begin <= end:#循环，此处的比较数与符号需是同一类型
        lst.append(begin)
        begin1 = datetime.datetime.strptime(begin, '%Y-%m-%d')#将str类型转换为datetime.datetime类型
        begin2=begin1+datetime.timedelta(days=1)#每次在前一日期基础上加一天
        begin=begin2.strftime('%Y-%m-%d')#将日期以字符串的形式显示
    return lst
if __name__ == '__main__':
    begin=input('请输入开始日期如2020-10-10')
    end=input('请输入结束日期2020-10-10')
    lst1=day_range(begin,end)
    print(lst1)
#时间戳转换为日期
#法一
import time
s=time.time()
s1=time.localtime(s)
s2=time.strftime('%Y-%m-%d %H:%M:%S',s1)
print(s2)
#法二
import time
s=time.time()#时间戳
b=datetime.datetime.fromtimestamp(s)
c=b.strftime('%Y-%m-%d %H:%M:%S')
print(c)

import time
#该方法与实际时间相差8个小时
s=time.time()
b=datetime.datetime.utcfromtimestamp(s)
c=b.strftime('%Y-%m-%d %H:%M:%S')
print(c)
"""
def fun(num,target):
        lens=len(num)
        for i in range(lens):
            if (target-num[i]) in num:
                if (target-num[i]==num[i])&(num.count(target-num[i])==1):
                    continue
                else:
                    j=num.index(target-num[i])
                    break
        if j>0:
            return [i,j]
        else:
            return []
if __name__ == '__main__':
    num=[11,2,7,15]
    target=9
    s=fun(num,target)
    print(s)