"""print('-------文件的打开--------')
file=open('test.txt','r')
print(file.readlines())
file.close()
print('---------文件的写入-------')
file1=open('b.txt','w')
file1.write('我爱你中国')
file1.close()
file2=open('b.txt','w')
file2.write('python') #如果文件存在，则写入的内容会覆盖原有的内容
file2.close()
print("--------文件的追加--------")
file3=open('c.txt','a')#如果文件不存在，则创建新的文件
file3.write("断桥残雪")
file3.close()
file4=open('b.txt','a')
file4.write('断桥残雪')
file4.close()#如果文件存在，则在其原有基础上追加
print('--------------二进制文件的读取---------------------')
start_file=open('b.txt','rb')#二进制文件的读
end_file=open('bc.txt','wb')#二进制文件的写
end_file.write('b.txt'.read())
start_file.close()
end_file.close()

print("------------文件对象的常用方法-----------------------")
#file=open('b.txt','r')
#print(file.read(10)) #read([size])可以设置读取多少的字节
#print(file.readline())#读取一行的文字
#print(file.readlines())#读取所有内容
print("----------------------")
#file=open('b.txt','w')
#print(file.write('张三'))#写入并覆盖原有内容
#lst=['张三','李四','王五']
#file.writelines(lst)#writelines写入列表
#file.close()
print("-------------------")
#file=open('b.txt','r')
#file.seek(2)#一个中文两个字节  seek表示从第几个字节开始输出
#print(file.read())
#file.seek(2,1)
#print(file.read())
#file.close()
#print(file.tell())#返回文件当前的指针，并说明共有多少个字节
file=open('b.txt','w')
print(file.write('张三'))
file.flush()#把缓冲区的内容写入，并且不关闭文件
print(file.write('高达周'))
file.close()#写入文件的同时，并关闭文件
print('----------with语句-----------------')
class Text:
    def __enter__(self):
        print("enter被调用")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit被调用')
        return self
    def show(self):
        print('show被调用')
        return self

with Text() as file:  #调用with语句时，会自动关闭文件
    file.show()

with open('b.txt','rb') as m:
    with open('d.txt','wb') as x:
        x.write(m.read())

#import os
#os.system('notepad.exe')#打开记事本
#os.system('calc.exe')#打开计算器
#os.startfile('C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe')#打开可执行文件
#print(os.getcwd())#查看其上一级文件名称
#print(os.listdir('package1'))#查看其文件名称下包含多少其他文件
#os.mkdir('v')#创建目录
#os.makedirs('fun/fun1/fun2')#创建多级目录
#os.rmdir('v')#删除目录
#os.removedirs('fun/fun1/fun2')#删除多级目录
#os.chdir('F:\\pycharm\\file\\september\\date.9.23') #修改文件路径
#print(os.getcwd())

print('------------------------')
import os.path
print(os.path.abspath('date.9.24.py'))#绝对路径
print(os.path.exists('n.txt'))#判断文件是否存在于该路径
print(os.path.exists('date.9.13.py'))
print(os.path.join('F:pycharm','c.txt'))#将文件和路径结合起来
print(os.path.splitext('date.9.24.py'))#分离文件名和扩展名
print(os.path.basename("F:\\pycharm\\file\\september\\date.9.23.py")) #提取文件名
print(os.path.dirname("F:\\pycharm\\file\\september\\date.9.23.py")) #提取路径名
print(os.path.isdir("F:\\pycharm\\file\\september\\date.9.23.py")) #判断其是否为当前路径

import os
path=os.getcwd()
lst=os.listdir(path)  #列表出其目录下所有的文件名
for file in lst:
    if file.endswith('.py'):
        print(file)

import os
path=os.getcwd()
lst=os.walk(path)  #列表出其目录下所有的文件名
for dirpath,dirname,filename in lst:
    print(dirpath)#获取路径
    print(dirname)#提取路径名
    print(filename)#文件名
    print('------------------')

age=int(input('请输入一个数字:'))
if age>=0 and age<=2:
    print("婴儿")
"""
a=input('请输入颜色')
