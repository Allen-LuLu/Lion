# 定义狮子类
class Lion:
    def __init__(self,swim_state,name,type = 'big'):
        self.isdanger = 0        # 判断狮子是否危险
        self.son = None          # 是否有儿子
        self.mom = None          # 是否有母亲
        self.isswim = swim_state  # 是否会游泳
        self.type = type         # 是大狮子还是小狮子
        self.name = name         #　名字

    # 设置儿子,s_state = 1会游泳，s_state = 0 不会游泳
    def setSon(self,s_state):
        self.son = Lion(s_state,name = self.name+'_son',type = 'small')
        self.son.mom = self
        return self.son

    # 判断自己是否是另外一只狮子的儿子
    def isSon(self,lion):
        if lion.son == self:
            return 1
        else:
            return 0
    # 判断自己是否是另外一只狮子的母亲
    def isMom(self,lion):
        if self.son == lion:
            return 1
        else:
            return 0

# 定义船
class Boat:
    def __init__(self):
        #　船上有两个位置
        self.seat1 = None
        self.seat2 = None

    # 上船
    def onBoat(self,lion1, lion2):
        self.seat1 = lion1
        self.seat2 = lion2
    # 移动，begin,end分别为起点和终点，应该为coast对象
    def move(self,begin,end):
        # 如果船上是一大一小，就要判断母子关系
        if self.seat1.type != self.seat2.type:
            if self.seat1.isSon(self.seat2) | self.seat1.isMom(self.seat2):
                print('{0} and {1} from {2} move to {3}'.format(self.seat1.name, self.seat2.name, begin.name, end.name))
                # 移动成功，从起点海岸删去移动走的狮子，在终点海岸布置移动过去的狮子
                begin.dellion(self.seat1,self.seat2)
                end.setlion(self.seat1,self.seat2)
                return 1
            else:
                print('can\'tmove')
                return 0
        # 如果船上只有一只狮子，只需判断船上的狮子是否会游泳
        elif self.seat1 == self.seat2:
            if self.seat1.isswim:
                print('{0}  from {1} move to {2}'.format(self.seat1.name,  begin.name, end.name))
                begin.dellion(self.seat1)
                end.setlion(self.seat1)
                return 1
            else:
                print('can\'tmove')
                return 0
        # 如果船上是两大或两小，则只需判断至少有一只狮子会游泳
        else:
            if self.seat1.isswim | self.seat2.isswim:
                print('{0} and {1} from {2} move to {3}'.format(self.seat1.name,self.seat2.name,begin.name,end.name))
                begin.dellion(self.seat1, self.seat2)
                end.setlion(self.seat1, self.seat2)
                return 1
            else:
                print('can\'tmove')
                return 0

# 定义海岸
class Coast:
    def __init__(self,name):
        # 海岸上有多少只狮子不确定，定义一个列表接收狮子
        self.seats = []
        self.name = name # 海岸的名字

    # 将狮子置于海岸上,*lion的意思是参数个数不定
    def setlion(self,*lions):
        for lion in lions:
            self.seats.append(lion)
    # 将狮子从海岸中移除
    def dellion(self,*lions):
        for lion in lions:
            self.seats.remove(lion)
    # 判断海岸上的狮子是否满足要求，不满足要求则返回1，代表gameover
    def isover(self):
        has_big = 0
        # 判断海岸上是否有大狮子，如果没有大狮子，小狮子必定安全
        for lion in self.seats:
            if lion.type == "big":
                has_big = 1

        for lion in self.seats:
        # 判断海岸上的小狮子是否危险，如果妈妈不在则小狮子有危险
            if lion.type == 'small':
                if lion.mom not in self.seats:
                    lion.isdanger = 1
                else:
                    lion.isdanger = 0
            # 如果小狮子有危险(即母亲不在同一个海岸)，且海岸上有大狮子，则小狮子必死，返回1
            if lion.isdanger & has_big:
                return 1
        # 如果没事,返回0
        return 0








if __name__ == '__main__':
    # 实例化6只狮子
    lion_a = Lion(1,name = 'lion_a')
    lion_a_son = lion_a.setSon(1)
    lion_b = Lion(1,name = 'lion_b')
    lion_b_son = lion_b.setSon(0)
    lion_c = Lion(1,name = 'lion_c')
    lion_c_son = lion_c.setSon(0)
    # 实例化两个海岸A和B
    coasta = Coast('A')
    coastb = Coast('B')

#########################################
# 下面的代码全是测试代码，可自行删除，主逻辑未实现
##########################################

    coasta.setlion(lion_a, lion_b,lion_c,lion_a_son,lion_b_son, lion_c_son)
    # print('coasta has lions:')
    # for i in range(len(coasta.seats)):
    #     print(coasta.seats[i].name)

    boat = Boat()
    boat.onBoat(lion_a_son, lion_b_son)
    boat.move(coasta, coastb)

    boat.onBoat(lion_a_son, lion_a_son)
    boat.move(coastb, coasta)

    boat.onBoat(lion_a_son, lion_c_son)
    boat.move(coasta, coastb)

    boat.onBoat(lion_a_son, lion_a_son)
    boat.move(coastb, coasta)

    boat.onBoat(lion_a_son, lion_a)
    boat.move(coasta, coastb)



    #print('\n',coasta.isover())

    # print('\nnow coasta has lions:')
    # for i in range(len(coasta.seats)):
    #     print(coasta.seats[i].name)
    #
    # print('\ncoastb has lions:')
    # for i in range(len(coastb.seats)):
    #     print(coastb.seats[i].name)






