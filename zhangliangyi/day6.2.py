def chagne_number( b ):
    print('函数中一开始 b 的值：{}' .format( b ) )
    b = 1000
    print('函数中 b 赋值后的值：{}' .format( b ) )
    
    
    b = 1
    chagne_number( b )
    print( '最后输出 b 的值：{}' .format( b )  )


num2 = 100
sum1 = lambda num1 : num1 + num2 ;

num2 = 10000
sum2 = lambda num1 : num1 + num2 ;

print( sum1( 1 ) )
print( sum2( 1 ) )

my_tuple = (1, 2, 3, 4, 5)
tuple_iter = iter(my_tuple)

# 使用迭代器遍历元组
for item in tuple_iter:
    print(item)

def count_down(n):
    print("倒计时开始！")
    while n > 0:
        yield n
        n -= 1
    yield "点火！"

# 创建生成器对象
counter = count_down(3)

# 逐个获取值
print(next(counter))  # 输出: 3
print(next(counter))  # 输出: 2
print(next(counter))  # 输出: 1
print(next(counter))  # 输出: "点火！"
# 再次调用next()会抛出StopIteration

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

# 创建列表
my_list = [1, 2, 3, 4, 5]

# 反转并转换为列表
reversed_list = list(reversed(my_list))
print(reversed_list)  # 输出: [5, 4, 3, 2, 1]

# 原始列表未被修改
print(my_list)        # 输出: [1, 2, 3, 4, 5]

s = "Hello, World!"
reversed_s = ''.join(reversed(s))
print(reversed_s)  # 输出: "!dlroW ,olleH"

names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]
for name, age in zip(names, ages):
     print(name,age)



names = ['laingdianshui', 'twowater', '两点水']
ages = [18, 19, 20]

dict1= dict(zip(names,ages))
print(dict1)

class ClassA():
    """这是一个示例类，演示类属性和实例属性的区别"""
    var1 = 100          # 类属性
    var2 = 0.01         # 类属性
    var3 = '两点水'      # 类属性

    def fun1(self):
        print('我是 fun1')
    def fun2(self):
        print('我是 fun2')
    def fun3(self):
        print('我是 fun3')

# 创建类实例
a = ClassA()
b = ClassA()

# 访问类属性（通过实例访问，会使用类属性）
print("通过实例访问类属性:")
print(a.var1)  # 100 (访问的是类属性)
print(b.var2)  # 0.01 (访问的是类属性)

# 调用实例方法
print("\n调用实例方法:")
a.fun1()  # 输出: 我是 fun1
b.fun3()  # 输出: 我是 fun3

# 修改类属性（所有实例都会受到影响）
print("\n修改类属性:")
ClassA.var1 = 200
print(a.var1)  # 200 (实例a现在使用新的类属性)
print(b.var1)  # 200 (实例b现在使用新的类属性)

# 为实例创建自己的属性（仅影响该实例）
print("\n为实例创建自己的属性:")
a.var3 = '三点水'  # 创建实例a的var3属性，覆盖类属性
print(a.var3)      # 三点水 (实例a使用自己的属性)
print(b.var3)      # 两点水 (实例b仍然使用类属性)

# 验证属性查找机制
print("\n验证属性查找机制:")
print("a.__dict__:", a.__dict__)  # 查看实例a的属性字典
print("b.__dict__:", b.__dict__)  # 查看实例b的属性字典
print("ClassA.__dict__:", ClassA.__dict__)  # 查看类的属性字典

# 检查类属性和实例属性的区分
print("\n检查属性类型:")
print("a.var1 是类属性吗?", a.var1 is ClassA.var1)  # True
print("a.var3 是类属性吗?", a.var3 is ClassA.var3)  # False




