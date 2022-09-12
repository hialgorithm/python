"""score=int(input("请输入一个数字:"))
if score<=100 and score>=90:
    print("A级")
elif score<=89 and score>=80:
    print("B级")
elif score<=79 and score>=70:
    print("C级")
elif score<=69 and score>=60:
    print("D级")
else:
    print("输入的成绩不在有效范围内")
"""

"""vip=input("你是会员吗:,y/n")
money=int(input("请输入金额:"))
if vip=='y':
    print("您是会员")
    if money>=200:
        print("打八折，购物金额为:",money*0.8)
    elif money>=100:
        print("打九折，购物金额为:",money*0.9)
    else:
        print("不打折，购物金额为:",money)

else:
    print("您不是会员")
    if money>=200:
        print("打九折，购物金额:",money*0.9)
    else:
        print("不打折:",money)
"""
num1=int(input("请输入数字:"))
num2=int(input("请输入数字:"))
"""if num1>=num2:
    print(num1,"大于等于",num2)
else:
    print(num1,"小于",num2)
    """
print(str(num1)+"大于等于"+str(num2) if num1>=num2 else str(num1)+"小于"+str(num2) )