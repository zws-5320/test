'''
继承的作用：重复的属性可以直接继承，无需再定义
class MyClass:  直接报错（__init__() should return None, not 'str'）
    def __init__(self):
        return "I love FishC.com!"
子类属性名称与父类相同：父类方法会被子类覆盖
子类不继承父类某个属性：子类中重写父类方法
super()不需要给出明确的基类的名称就可以所有基类的方法，当需要改变继承关系只需要该拜年父类即可


class Brid:
    def __init__(self):
        self.x = 0
    def fly(self):
        print('fly,fly')
    def eat(self):
        print('eat')
class Penguin(Brid):
    def __init__(self):
        super().__init__()
    def fly(self):
        pass
peng = Penguin()
peng.eat()
peng.fly()

0. 定义一个点（Point）类和直线（Line）类，使用 getLen 方法可以获得直线的长度。)
设点 A(X1,Y1)、点 B(X2,Y2)，则两点构成的直线长度 |AB| = √((x1-x2)2+(y1-y2)2)
Python 中计算开根号可使用 math 模块中的 sqrt 函数
直线需有两点构成，因此初始化时需有两个点（Point）对象作为参数


import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Line():
    def __init__(self, p1, p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()
        self.len = math.sqrt(self.x*self.x + self.y*self.y)

    def getLen(self):
        return self.len
p1 = Point(1,1)
p2 = Point(4,5)
line = Line(p1,p2)
line.getLen()
'''
class Lx():
    def __init__(self,x=1,y=2):
        self.x = x
        self.y = y
    def test_1(self):
        self.x = self.x + self.y
        return self.x
    def test_2(self):
        self.y = self.x - self.y
        return self.y
    def tets_0(self):
        self.q = self.x * self.y
        return self.q
class Ly():
    def __init__(self,p1,p2):
        self.x = p1.test_1() * p2.test_1()
        self.y = p1.test_2() + p2.test_2()
    def test_3(self):
        self.z = p1.tets_0() + p2.tets_0 ()
        return self.z
p1 = Lx(9,1)
p2 = Lx(0,9)
ly = Ly(p1,p2)
print(ly.test_3())