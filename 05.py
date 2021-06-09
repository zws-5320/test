#encoding:utf-8
'''
def runnian(n):
    if n %4==0 and n%100!=0:
        print('n为闰年')
    elif n%400:
        print('n为闰年')
    else:
        print('n不为闰年')
number = int(input("请输入"))
runnian(number)
'''
import random as r
x_1=[0,10]
x= r.randint(0,1)
print(x)
new_x = x + r.choice([1,2,-1,-2])
print(new_x)
if new_x <=10 and new_x>=0:
    new_x =new_x
else:
    while new_x >10:
        new_x = new_x +r.choice([-1.-2])
    while new_x<0:
        new_x = new_x+r.choice([1,2])
print(new_x)