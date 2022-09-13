"""sum=0
a=0
while a<5:
    sum=sum+a
    a=a+1
print("sum=",sum)"""
'''sum=0
a=0
while a<=100 :
    if a%2==0:
    if not bool(a%2):
    if  bool(a % 2):
        sum = sum + a
        a+=1
    else:
        a+=1
print("sum=",sum)'''
"""r=range(2,10,2)
print(r)
print(list(r))
x=range(10)
print(list(x))
s=range(1,10)
print(list(s))

for a in "python":
    print(a)
for g in range(1,10,2):
    print(g)
for _ in range(10):
    print("好好学习，天天向上")"""
"""sum=0
for x in range(0,100,2):
    sum=sum+x
for x in range(1,101):
    if x%2==0:
        sum+=x
        x+=1
    else:
        x+=1
print(sum)"""


"""100-999水仙花数"""
"""for i in range(100,1000):
    if i == (i%10)**3+(i//10%10)**3+(i//100)**3:
        print(i)
"""

"""for i in range(100,1000):
    ge=i%10
    shi=(i//10)%10
    bai=i//100
    #print(ge,shi,bai)
    if ge**3+shi**3+bai**3==i:
        print(i)
"""
"""for i in range(3):
    my=input("请输入密码:")
    if my=="8888":
        print("密码正确")
        break
    else:
        print("密码不正确")
"""
"""a=0
while a<3:
    my = input("请输入密码:")
    if my=="8888":
        print("密码正确")
        break
    else:
        print("密码错误:")
    a+=1

for i in range(1,51):
    if i%5==0:
        print(i)
print("----------------------")
for x in range(1,51):
    if x%5!=0:
        continue
    print(x)

for i in range(3):
    se=input("请输入密码:")
    if se=="8888":
        print("密码正确:")
        break
    else:
        print("密码错误:")
else:
    print("三次输入均错误")

a=0
while a<3:
    my=input("请输入密码:")
    if my=="8888":
        print("密码正确")
        break
    else:
        print("密码错误:")
    a+=1
else:
    print("三次密码输入均错误")

for i in range(4):
    for j in range(5):
        print("*",end='\t')
    print('\n')


for i in range(1,10):
    for j in range(1,i+1):
        print(i, "*", j, "=", i * j, end="\t")
    print()

i=1

while i<=9:
    j = 1
    while j<=i:
        print(i,"*",j,"=",i*j,end="\t")
        j+=1
    i += 1
    print()

for x in range(1,5):
    for y in range(1,x+1):
        print("*",end="\t")
    print("\n")
"""
lst=["hello","GaoFei","hei"]
print(lst)
print(lst[2])
print(lst.index("hei"))

lst2=list(["hello","world"])
#print(lst2)
print(lst2.index('hello'))





