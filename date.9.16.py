#--------集合---------------
s={1,2,3,4,5,6,7}
print(s,type(s))#第一种创建集合的方式
s1=set([12,34,56,87])
print(s1,type(s1))
s2=set(range(6))
print(s2,type(s2))
s3=set({1,34,6,5,5,6})
print(s3,type(s3))
s4=set((45,3,3,54,6,8,8))
print(s4,type(s4))
s5=set("python")
print(s5,type(s5))
s6=set()
print(s6,type(s6))
s7={}
print(s7,type(s7))#dict类型
print("-----集合元素的判断-----")
s={1,23,45,56,78,54,43}
print(1 in s)
print(23 not in s)
print(100 not in s)
print("-------集合元素的增加-------")
s.add(100)
print(s)
s.update((122,123))
print(s)
s.update([3,6])
print(s)
s.update({1,2,3,4})
print(s)
print("--------集合元素的删除-------------")
s.remove(1)#一次只可以删除一个元素
print(s)

s.pop()
s.pop()
print(s)

s.discard(89)
print(s)
s.discard(78)#   discard删除元素时，如果该元素不在集合范围内也不会报错
print(s)

s.clear()
print(s)

s1={1,2,3,4,6}
s2={1,2,3}
s3={1,2,6,8}
print(s3.issubset(s1))
print(s2.issuperset(s1))#issuperset 超集
print(s2.issubset(s1)) #issubset子集
print(s1.issuperset(s2))
print(s2.isdisjoint(s3)) #如果有交集则显示为flase
s4={9,10}
print(s4.isdisjoint(s1)) #如果无交集则显示为ture

c1={10,20,30}
c2={10,40,80,20}
c3={10,30,50,70}
print(c1.intersection(c2))
print(c1&c2)#c1与c2交集
print(c1.union(c2))
print(c1|c2)#c1与c2并集
print(c1.difference(c2))
print(c1-c2)#c1与c2的差集
print(c1.symmetric_difference(c2))
print(c1.symmetric_difference(c3))
print(c3^c2)#对称差集

x1={i for i in range(6)}
print(x1)
x2={i for i in [1,2,3,4]}
print(x2)
x3={i for i in {1,2,3,4,5,6,7}}
print(x3)