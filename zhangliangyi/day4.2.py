class ClassA():
    var1 = 100
    var2 = 0.01
    var3 = '两点水'

    def fun1():
        print('我是 fun1')
    def fun2():
        print('我是 fun1')
    def fun3():
        print('我是 fun1')


#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


if __name__ == '__main__':
    userInfo = UserInfo('两点水', 23, 347073565);
    # 打印所有属性
    print(dir(userInfo))
    # 打印构造函数中的属性
    print(userInfo.__dict__)
    print(userInfo.get_account())
    # 用于验证双下划线是否是真正的私有属性
    print(userInfo._UserInfo__account)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class User(object):
    def upgrade(self):
        pass

    def _buy_equipment(self):
        pass

    def __pk(self):
        pass



