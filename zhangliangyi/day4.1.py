# -*- coding: UTF-8 -*-
gen= (x * x for x in range(10))

for num  in  gen :
	print(num)
	
# -*- coding: UTF-8 -*-
def my_function():
    for i in range(10):
        yield i

# -*- coding: UTF-8 -*-
def my_function():
    for i in range(10):
        yield i

print(my_function())

# -*- coding: UTF-8 -*-
def odd():
    print ( 'step 1' )
    yield ( 1 )
    print ( 'step 2' )
    yield ( 3 )
    print ( 'step 3' )
    yield ( 5 )

o = odd()
print( next( o ) )
print( next( o ) )
print( next( o ) )


# -*- coding: UTF-8 -*-
def triangles( n ):         # 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [ L [ i -1 ] + L [ i ] for i in range (len(L))]

n= 0
for t in triangles( 10 ):   # 直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break

list1 = [1,2,3,4,5]
for num1 in reversed(list1) :
    print ( num1 , end = ' ' )
#颠倒

# -*- coding: UTF-8 -*-

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
    	# Forward iterator
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
    	# Reverse iterator
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(30)):
    print(rr)
for rr in Countdown(30):
    print(rr)

# -*- coding: UTF-8 -*-

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
for name, age in zip(names, ages):
     print(name,age)


# -*- coding: UTF-8 -*-

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]

dict1= dict(zip(names,ages))

print(dict1)











