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
    pass
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
    pass
def total():
    pass
def show():
    pass

if __name__ == '__main__':
    main()