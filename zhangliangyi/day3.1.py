def sum (a,b):
    return a + b
print(sum(3,5))

a = sum(3,5)
print(a)


def  division ( num1, num2 ):
	# 求商与余数
         a = num1 % num2
         b = (num1-a) / num2
         return b , a

num1 , num2 = division(9,4)
tuple1 = division(9,4)

print (num1,num2)
print (tuple1)

def print_type(name,age,sex = '男'):
    print('名字是:{}'.format(name),end = ' ' )
    print('年龄是:{}'.format(age),end = ' ' )
    print('性别是:{}'.format(sex))  
       
print_type('两点水',18, '女')
print_type('小明',20)   


a = [1, 2]
b = [3, 4]
a.append(b)  # 将整个 b 列表作为元素添加

print(a)  # 输出: [1, 2, [3, 4]]

c = []
c.append(a)
c.append(b[0])
print(c)  # 输出: [[1, 2, [3, 4]], 3]

# -*- coding: UTF-8 -*-

def print_user_info( name ,  age  , sex = '男' , * hobby):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info( '两点水' ,18 , '女', '打篮球','打羽毛球','跑步')

# -*- coding: UTF-8 -*-

def print_user_info( name ,  age  , sex = '男' , ** hobby ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex) ,end = ' ' )
    print('爱好：{}'.format(hobby))
    return;

# 调用 print_user_info 函数
print_user_info( name = '两点水' , age = 18 , sex = '女', hobby = ('打篮球','打羽毛球','跑步'))

# -*- coding: UTF-8 -*-
def chagne_number( b ):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b = 1000
    print('函数中 b 赋值后的值：{}' .format( b ) )


b = 1
chagne_number( b )
print( '最后输出 b 的值：{}' .format( b )  )

# -*- coding: UTF-8 -*-

def chagne_list( b ):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b.append(1000)
    print('函数中 b 赋值后的值：{}' .format( b ) )


b = [1,2,3,4,5]
chagne_list( b )
print( '最后输出 b 的值：{}' .format( b )  )

# -*- coding: UTF-8 -*-

num2 = 100
sum1 = lambda num1 : num1 + num2 ;

num2 = 10000
sum2 = lambda num1 : num1 + num2 ;

print( sum1( 1 ) )
print( sum2( 1 ) )













