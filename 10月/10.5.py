"""
class Fun():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def start(self):
        pass
    def end(self):
        pass

class Taxi(Fun):
    def __init__(self,name,id,car):
        super().__init__(name,id)
        self.car=car
    def start(self):
        print('你好')
        print(f'我是{self.name},我的车牌是{self.id},我的汽车是{self.car},你要去哪里？')
    def end(self):
        print('目的地到了，欢迎下次光临')

if __name__ == '__main__':
    name=input('请输入名称')
    id=input('请输入车牌')
    car=input('请输入车子品牌')
    taxi=Taxi(name,id,car)
    taxi.start()
    taxi.end()
"""
import datetime
def timedate():
    day=input('请输入日期20221005')
    day=day.strip()
    dates=day[0:4]+'-'+day[4:6]+'-'+day[6:8]
    return datetime.datetime.strptime(dates,'%Y-%m-%d')
if __name__ == '__main__':
    print('------------------')
    t=timedate()
    a=int(input('请输入间隔天数'))
    y=t+datetime.timedelta(days=a)
    print('推算的日期为:'+str(y))
