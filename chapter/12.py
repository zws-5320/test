'''
a+b中的的 + 调用的是__add__实际函数是sub
a-b中的的 - 调用的是__sub__实际函数是add


class New_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)
    def __sub__(self,other):
        return int.__add__(self,other)
a = New_int(3)
b = New_int(5)
print(a+b)
print(a-b)
'''
'''
定制一个计时器的类
start和stop方法代表启动计时跟停止计时
假设计时器对象t1，print（t1）和直接调用t1均显示结果
当计时器未启动或已经停止计时，调用stop方法会给予温馨的提示
两个计时器对象可以进行相加：t1+t2
'''