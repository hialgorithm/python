"""print("-------------模块的导入--------------")
import math
print(math)
print(type(math))
print(id(math))
print(dir(math))
print('模块的调用')
print(math.ceil(9.05))
print(math.asin(0.5))
print(math.exp(2))
print(math.pi)
print(math.floor(9.98))
print("-------------------------")
from math import pi
print(pi)
print(pow(2,3))
print(math.pow(2,3))
from math import pow
print(pow(2,3))
print("----------从其他模块导入----------")
import test
print(test.fun1(10,20))
print(test.fun2(10,20))
from test import fun1
from test import fun2
print(fun1(3,9))
print(fun2(3,8))
print("--------------")
import test
print(test.add(20,40))

import package1.module_A
print(package1.module_A.a)
print("------------------")
import  package1.module_B as ab #ab为其重命名
print(ab.b)
"""
import package1
import test
print("----------")
from package1 import module_A
from package1.module_B import b
print("----------------")
import sys
print(sys.getsizeof(45))
print(sys.getsizeof(12))
print(sys.getsizeof(0))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print("-----------------")
import time
print(time.time())
print(time.localtime(time.time()))
print("-----------")
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())
print("-----------------")
