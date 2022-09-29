
"""
lst=[82,88,98,86,92,0,99]
for index,year in enumerate(lst):
    if year!=0:
       lst[index]='19'+str(year)
    else:
        lst[index]='200'+str(year)
print(lst)
lst.sort()
print(lst)

lst=[]
for i in range(0,5):
    good=input('每次只可以入库一个产品')
    lst.append(good)
for item in lst:
    print(item)
car=[]
while True:
    num=input('请输入商品编号')
    for item in lst:
        if item.find(num)!=-1:
            car.append(item)
            break
    if num=='q':
        break
print('商品为:')
#for i in car:
 #   print(i)
for i in range(len(car)-1,-1,-1):
    print(car[i])

lst=[]
for i in range(0,5):
    food=input('请输入商品编号')
    lst.append(food)
for item in lst:
    print(item)
car=[]
while True:
    i1=input('请输入需要添加的物品编号')
    for item in lst:
        if item.find(i1)!=-1:
            car.append(item)
            break
    if i1=='k':
        break
for i2 in range(len(car)-1,-1,-1):
    print(car[i2])

lst=dict({'狮子座': '胆大心细', '金牛座': '固执内向', '处女座': '细心'})
print(type(lst))
key=input('请输入')
for item in lst:
    if item == key:
        print(key,"特点为:",lst.get(key))


lst=('狮子座','金牛座','处女座')
l=('胆大心细','固执内向','细心')
d=dict(zip(lst,l))
print(d)
star=input('请输入你的星座')
for item in d:
    if item==star:
        print(star,"特点为:",d.get(star))
        break
else:
    print('输入错误')

lst={'G1567': ['北京站-上海站','9::00','17:00','9小时']}
print('车次\t出发站-到达站\t出发站\t到达站\t历时时长')
for item in lst:
    print(item,end=' ')
    for i in lst[item]:
        print(i,end=' ')
    inf=input("请输入购买的车次")
    peo=input('请输入乘车人信息')
    if inf==item:
        print('购买成功')
    else:
        print('购买失败')

lst={'1.':'蓝山','2.':'卡布奇诺','3.':'拿铁','4.':'皇家咖啡','5':'女王咖啡'}
print('你好，欢迎光临小猫咖啡馆')
print('本店经营的咖啡有:')
print(lst)
chose=input('请输入您的选择')
for item in lst:
    if chose==item:
        print(f'你的咖啡{lst.get(chose)}到了')

lst=('蓝山','卡布奇诺','拿铁','皇家咖啡','女王咖啡')
print('你好，欢迎光临小猫咖啡馆')
print('本店经营的咖啡有:')
print(lst)
for index,item in enumerate(lst):
    print(index+1,item,end=' ')
num=int(input('请选择编号'))
if 0<=num<=len(lst):
    print(f'你的{lst[num-1]}到了')
"""
lst=(('广大恒大',72),('北京国安',70),('上海上港',66),('江苏苏宁',53),('山东鲁能',51))
for index,item in enumerate(lst):
    print(index+1,end=' ')
    for score in item:
        print(score,end=' ')



