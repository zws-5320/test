'''
0. 什么是组合（组成）？在class __init__中直接实例化其他class，例如：self.a = A(x)
1. 什么时候用组合，什么时候用继承？继承单个class时使用，组合可以多重组合，复用多个class的方法
3. 如果对象的属性跟方法名字相同，会怎样？对象的属性会覆盖方法
4. 请问以下类定义中哪些是类属性，哪些是实例属性？self.x/y是类的属性；C.count是实例属性
class C:
        num = 0
        def __init__(self):
                self.x = 4
                self.y = 5
                C.count = 6
5. 请问以下代码中，bb 对象为什么调用 printBB() 方法失败？绑定bb.printBB()会将bb作为参数传入
class BB:
        def printBB():
                print("no zuo no die")
>>> bb = BB()
>>> bb.printBB()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    bb.printBB()
TypeError: printBB() takes 0 positional arguments but 1 was given
1. 定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构。至少需要有以下方法：
isEmpty()   判断当前栈是否为空（返回 True 或 False）
push()  往栈的顶部压入一个数据项
pop()   从栈顶弹出一个数据项（并在栈中删除）
top()   显示当前栈顶的一个数据项
bottom()    显示当前栈底的一个数据项
'''
class Stack():
    def __init__(self,y):
        self.x = ['F','i','s','h','C']
        self.y = y
    def isEmpty(self):
        if len(self.x)!=0:
            return True
        else:
            False
    def push(self):
        self.x = self.x.insert(0,self.y)
    def pop(slef):
        slef.x = slef.pop(0)
    def top(slef):
        print(slef.x[0])
    def bottom(slef):
        print(slef.x[-1])