

# name = input('请输入您的姓名:')
# name1 = f'hello,{name}'
# print(name1)
# name2 = 'hello,{}'.format(name)
# print(name2)

name = ['day1','day2','day3','day4']
print(name[0])
print(name[0:1])

class ClassA():
    var1 = '两点水'

    @classmethod
    def fun1(cls):
        print('var1 值为：' + cls.var1)


ClassA.fun1()

str3 = '两\'点\'水'
print(str3)

str5 = 4/2
print(type(str5))

str6 = 4**2
print(str6)

print(int (88.88))

a,b,c = 1 , 87.45 , 'zhangsan'
print(a,b,c)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 旧式类
class OldClass:
    def __init__(self, account, name):
        self.account = account
        self.name = name


# 新式类
class NewClass(object):
    def __init__(self, account, name):
        self.account = account
        self.name = name


if __name__ == '__main__':
    old_class = OldClass(111111, 'OldClass')
    print(old_class)
    print(type(old_class))
    print(dir(old_class))
    print('\n')
    new_class = NewClass(222222, 'NewClass')
    print(new_class)
    print(type(new_class))
    print(dir(new_class))

