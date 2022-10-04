import math
"""
class Instrument():
    def make_soude(self):
        pass
class Erhu(Instrument):
    def make_soude(self):
        print('二胡在发声')
class Piano(Instrument):
    def make_soude(self):
        print('钢琴在发声')
def play(instrument):
    instrument.make_soude()
class Bird():
    def make_soude(self):
        print('小鸟在发声')

if __name__ == '__main__':
    play(Erhu())
    play(Piano())
    play(Bird())
    
class Fun():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def start(self):
        pass
    def end(self):
        pass

class Taxi(Fun):
    def __init__(self,name,id,w):
        super().__init__(name,id)
        self.w=w
    def start(self):
        print('您好')
        print(f"我是{self.name},车牌号是{self.id},你要去哪里")
    def end(self):
        print('目的地到了，请付费下车')
class Family(Fun):
    def __init__(self,name,id,w):
        super().__init__(name,id)
        self.w=w
    def start(self):
        print(f'我是{self.name},车牌是{self.id}，我的汽车我做主')
    def end(self):
        print('目的地到了')
if __name__ == '__main__':
    taxi=Taxi('大众','江13456w','chan')
    taxi.start()
    taxi.end()
    F=Family('奥迪','沪12345','shu')
    F.start()
    F.end()
    """
import prettytable as pt
def show_table(row_num):
    table=pt.PrettyTable()
    table.field_names=['行号','坐位1','坐位2','坐位3','坐位4','坐位5']
    for i in range(row_num):
        lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
        table.add_row(lst)
    print(table)
def buy(row_num,row,colunm):
    table = pt.PrettyTable()
    table.field_names = ['行号', '坐位1', '坐位2', '坐位3', '坐位4', '坐位5']
    for i in range(row_num):
        if i+1==row:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            lst[colunm]='已售'
            table.add_row(lst)
        else:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            table.add_row(lst)
    print(table)




if __name__ == '__main__':
    row_num=13
    show_table(row_num)
    row=int(input('请输入行数'))
    colunm=int(input('请输入座位号'))
    buy(row_num,row,colunm)

