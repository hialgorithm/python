"""lst=[0,10,20,30,40,50,60,70,80,90]
print(lst[2:10:1])
print(lst[:5:])
print(lst[::1])
print(lst[1::2])
lst2=lst[1:5:2]
print(id(lst))
print(id(lst2))
print("--------------------------")
print(lst[::-1])
print(lst[10::-2])
print(lst[:10:-1])
print(lst[9:1:-2])
for a in lst:
    print(a)
print(----------列表元素的增加--------------)
lst.append(111)
print(lst)
lst2=[111,111,222,'hello','world']
#lst.extend(111,111,222,'hello','world') 错误
lst.extend(lst2)
print(lst)
lst.insert(1,'helllo')
print(lst)
lst[1:2:1]=lst2
print(lst)
"""
"""print("----------列表元素的删除-------------")
lst=[10,20,30,40,"hello","world",30]
lst.remove(30) #删除一个元素，若有相同的的元素则删除第一个元素
print(lst)
lst.pop(4)
print(lst) #通过元素下表来删除元素
lst.pop() #不指定下标的话，则删除最后一个元素
print(lst)
lst[1:2]=[] #删除的位置置为空格
print(lst)
lst.clear()#清空列表
print(lst)
lst.del()
print(lst)

print("---------列表元素的修改--------")
lst=[1,2,3,54,5,7,8]
lst[4]=100
print(lst)
lst[1:3]=100,200,3000
print(lst)
"""
print("-----------排序----------")
lst=[5,7,2,87,432,76,12]
"""lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

lst2=sorted(lst)
print(lst2)
lst2=sorted(lst,reverse=True)#倒序
print(lst2)
lst2=sorted(lst,reverse=False) #正序
print(lst2)
lst3=[i*2 for i in range(1,9)]
print(lst3)
lst4=[1,2,3,4,5,6]"""
print(lst.index(5))




