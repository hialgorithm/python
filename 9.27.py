"""
import os
filename='student.txt'
def main():
    while True:
        menu()
        num=int(input("请输入数字:"))
        if num in [0,1,2,3,4,5,6,7]:
            if num==0:
                answer=input('确定要退出吗？y/n')
                if answer=='y' or answer=="Y":
                    print("退出，感谢使用")
                    break
                else:
                    continue
            if num==1:
                insert()
            if num==2:
                search()
            if num==3:
                delete()
            if num==4:
                modify()
            if num==5:
                sort()
            if num==6:
                total()
            if num==7:
                show()

def menu():
    print("-------------------------------学生管理系统------------------------")
    print("--------------------------------功能菜单--------------------------")
    print("\t\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t\t0.退出")
    print('----------------------')

def insert():
    student_list=[]#创建一个空列表
    while True:
        id=input('请输入学号:(列:1001)')
        if not id:
            continue #使用continue会重新输入id  若使用break就会程序结束从头开始运行
        name=input("请输入学生姓名:")
        if not name:
            continue
        #以上内容是输入id与姓名
        try:
            english=int(input("请输入英语成绩"))
            python=int(input("请输入python成绩"))
            java=int(input("请输入java成绩"))
        except:
            print("输入的成绩无效，请重新输入:")
            continue
        #以上内容是输入成绩
        student={'id':id,'name':name,'english':english,'python':python,'java':java}#将成绩输出为字典形式
        student_list.append(student)#在列表中追加
        answer=input("是否继续添加成绩:y/n\n")
        if answer=='y' or answer=='Y':
            continue
        else:
            break
        #以上内容是询问是否添加，若添加则继续，若不添加则录入成绩程序结束
    save(student_list)#保存成绩及调用save函数
    print('成绩录入完成')

def save(lst):
    try:
        stu_txt=open(filename,'a',encoding='UTF-8')
    except:
        stu_txt=open(filename,'w',encoding='UTF-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    student_query=[]
    id=''
    name=''
    while True:
        if os.path.exists(filename):
            mode=input('按id查找请输入1，按姓名查找请输入2')
            if mode=='1':
                id=input('请输入学生id')
            elif mode=='2':
                name=input('请输入学生姓名')
            else:
                print('输入的信息有误')
                continue
            with open(filename,'r',encoding='utf-8') as rfile:
                student_r=rfile.readlines()
                for item in student_r:
                    d=dict(eval(item))
                    if id!='':
                        if d['id']==id:
                            student_query.append(d)
                    if name!='':
                        if d['name']==name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer=input('是否继续查询y/n\n')
            if answer=='y' or answer=='Y':
                continue
            else:
                break
        else:
            print('磁盘中午文件信息')
            return

def show_student(lst):
    if len(lst)==0:
        print("没有信息")
        return

    format_title='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('id', 'name', '英语成绩', 'python成绩', 'java成绩','总成绩'))
    format_date='{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_date.format(item.get('id'),
                                item.get('name'),
                                item.get('english'),
                                item.get('python'),
                                item.get('java'),
                                int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                ))

def delete():
    while True:
        stu_id=input('请输入学生id:')
        if stu_id !='':#判断输入的id是否为空字符串
            if os.path.exists(filename):
                with open(filename,'r',encoding='utf-8') as file: #如果不是空字符串，则将文件中的信息读取出来
                    stu_old=file.readlines()
        else:
            stu_old=[]   #如果是空字符则复值为空集合
        flag=False  #用来判断是否删除成功，默认为未删除
        if stu_old:      #若stu_old不为空集合，则执行下列代码
            with open(filename,'w',encoding='utf-8') as newfile:   #文件以只写的形式打开，并且重新命名为newfile
                d={}     #创建一个空集合，用来放置删除信息后的位置
                for item in stu_old:
                    d=dict(eval(item))       #将stu_old中的信息转为字典型
                    if d['id']!=stu_id:        #判断输入的id与文件中的id是否一致，如果与输入的id不一致，则将其以字符串的形式写入newfile中
                        newfile.write(str(d)+'\n')
                    else:
                        flag=True     #若一致，则flag为Ture
                if flag:          #这里是用来判断是否已经删除
                    print(f'信息{stu_id}已经被删除')
                else:
                    print(f'找不到对应id{stu_id}信息')
        else:     #若stu_old为空集合，则执行下列代码
            print("没有学生的信息")
            break
        show()
        answer=input('是否继续删除学生信息y/n\n')
        if answer=='y' or answer=='Y':
            continue
        else:
            break

def modify():
    show()#将信息显示出来
    if os.path.exists(filename):         #判断磁盘中是否存在该文件
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old=rfile.readlines()          #如果存在，则将其进行读取
    else:
        return         #如果磁盘中无此文件，则结束程序
    student=input('请输入id:')           #开始输入需要修改的id
    with open(filename,'w',encoding='utf-8') as wfile:
        for item in student_old:    #在读取的文件中遍历
            d=dict(eval(item))      #将遍历的文件改成字典类型
            if d['id']==student:     #判断输入的id与遍历的id是否一致
                print('可以修改信息')
                while True:          #信息一致时，开始进入循环
                    try:
                        d['name']=input('请输入姓名')
                        d['english']=input('请输入英语成绩')
                        d['python']=input('请输入python成绩')
                        d['java']=input('请输入java成绩')
                    except:
                        print('信息错误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')     #将修改之后的信息写入文件中
                print('修改信息成功')
            else:
                wfile.write(str(d) + '\n')   #如果输入的id与磁盘中id不一致，则将原内容写入
    anwser=input('是否继续修改信息:y/n\t')
    if anwser=='y' or anwser=="Y":
        modify()

def sort():
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as sfile:
            student_s=sfile.readlines()
            for item in student_s:
                student_lst.append(eval(item))
    else:
        return
    asc_or_desc=input('请选择排序方法:1:降序0:升序')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('输入有误，请重新输入')
        return
    mode=input('请选择排序方式:1:英语排序 2:python排序 3:java排序 4:总成绩排序')
    if mode=='1':
        student_lst.sort(key=lambda student_lst:student_lst['english'],reverse=asc_or_desc_bool)
    elif mode=='2':
        student_lst.sort(key=lambda student_lst: student_lst['python'], reverse=asc_or_desc_bool)
    elif mode=='3':
        student_lst.sort(key=lambda student_lst:student_lst['java'],reverse=asc_or_desc_bool)
    elif mode=='4':
        student_lst.sort(key=lambda student_lst:int(student_lst['english'])+
                                                int(student_lst['python'])+
                                                int(student_lst['java'])
                                                ,reverse=asc_or_desc_bool)
    else:
        print('输入错误，请重新输入')
        sort()
    show_student(student_lst)

def total():
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as afile:
            student_t=afile.readlines()
            if student_t:
                print(f'共有{len(student_t)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('文件不存在')
        return

def show():
    d = []
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as sfile:
            student_s=sfile.readlines()
            for item in student_s:
                #如果d=[]写在此处在只会显示一条信息
                d.append(eval(item))
            if d:
                show_student(d)
            else:
                return
    else:
        print('暂未保存信息')
        return

if __name__ == '__main__':
    main()
"""
"""
1
file1=open("F:/pycharm/file/a.txt",'w')
print('奋斗成就更好的你',file=file1)
file1.close()
2
file1=open("F:/pycharm/file/a.txt",'w')
file1.write('我爱你中国')
file1.close()
3
with open("F:/pycharm/file/a.txt",'w') as file:
    file.write("高菲")
print('星期日','今天')
print('------------------------------------')
print('08时','11时','14时','17时','20时','23时')
print('0℃','6℃','10℃','4℃', '1℃', '0℃')
print('------------------------------------')
print('明天','2/23','2℃/11℃')

name1='张三'
name2='李四'
name3='王五'
name4='赵六'
name5='孙七'
print('➀\t'+name1)
print('➁\t'+name2)
print('➂\t'+name3)
print('➃\t'+name4)
print('➄\t'+name5)

print('------------------------')
lst_name=['张三','李四','王五','赵六','孙七']
lat_id=['➀','➁','➂','➃','➄']
for i in range(5):
    print(lat_id[i]+lst_name[i])
"""
print('----------------')
lst_name=['张三','李四','王五','赵六','孙七']
lat_id=['➀','➁','➂','➃','➄']
for id,name in zip(lat_id,lst_name):
    print(id,name)
print('---------------')
d={'➀':'张三','➁':'李四','➂':'王五','➃':'赵六','➄':'孙七'}
for item in d:
    print(item,d[item])