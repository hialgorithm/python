"""字典的创建及使用"""
"""什么是字典:字典是以键值对的方式存储数据。例如：score={"张三":100,"李四":98}  以逗号来区别不同的数据
python 中字典是通过键入的key来查找value的位置"""
"""print("-----第一种创建方式-------")
score={"张三":20,"李四":67}
print(score)
print(type(score))
#第二种创建方式
score2=dict(name='张三',age=20)
print(score2)
#空字典
score3={}
print(score3)
print(score['李四'])#第一种方式
#print(score["王五"]）使用[]时 若没有这个值则会报错
print(score.get("张三"))#第二种方式
print(score.get("张三",90))
print(score.get("王五"))#使用get时 若没有这个值则会显示none
print(score.get("王五",99))#使用get时 若没有这个值 可以设置数字来显示

print(20 in score)#只能通过key来判断是否在范围内，value不可以
print("张三" not in score)
print("张三" in score)

del score["张三"]
print(score)# 删除一个key-value对

score.clear()#清空字典
print(score)

score["王五"]=90
print(score)#增加key-value对

score["王五"]=100
print(score)#修改ket-value对

score4={"张三":38,"李四":89,"王五":90,"麻溜":97}
k=score4.keys()
print(k)
print(type(k))
print(list(k))

v=score4.values()
print(v)
print(list(v))

i=score4.items()
print(i)

for item in score4:
    print(item,score4[item],score4.get(item))

score7={"张三":20,"张三":90}#key不能重复
print(score7)
score9={"张三":90,"张四":90}#value可以重复
print(score9)

items=["张三那","李四","网速"]
lk=[10,20,30]
lst=zip(items,lk)
print(list(lst))#法一 字典生成试
#d={item.upper():price for item,price in zip(items,lk)} 法二 字典生成试
#print(d)

print("------元组-------")
t=("python","kdfhsk","hjfhg")#第一种方式
print(t)
t1="python","kdfhsk","hjfhg"
print(t1)
t2="python"
print(type(t2))
print(t2)
t3=("python")
print(type(t3))
print(t3)
t4=("python",)
print(type(t4))  #如果元组中只有一个元素，需要在元素后面添加“，”
print(t4)

t5=tuple("python","hfgdkj")#第二种方式
print(t5)"""

x=("th","啥叫","就很恐怖v",[789,6,8])
print(x[0],type(x[0]))
print(x[1],type(x[1]))
print(x[2],type(x[2]))
print(x[3],type(x[3]))
x[3].append(100)
print(x)
for i in x:
    print(i)