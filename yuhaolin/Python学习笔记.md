# 变量和简单数据类型

## 变量

```python
message = "hello world!"
print(message)
```

## 字符串

字符串(string)就是一串字符。在Python中用引号引起的都是字符串（单、双引号都可以）

```python
"This is a string."
'This is a string.'
```
### 使用方法修改字符串的大小写

```python
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
```
### 在字符串中使用变量

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
```
结果如下
```
ada lovelace
```
> ***要在字符串中插入变量的值，可先在左引号前加上字母f，要将要插入的变量放在花括号内，这样py在显示字符串时，会把每个变量替换成其值，这成为f字符串，f是format简写***

可以用f字符串实现很多任务
#### 01
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"hello, {full_name.title()}!")
```
> 这串代码实现了一个格式良好的问候语

```
hello, Ada Lovelace!
```

#### 02创建消息
```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"hello, {full_name.title()}!"
print(message)
```

### 使用制表符或换行符来添加空白

```python
print("languages:\n\tPython\n\tC\n\tJavaScript")
```
结果
```
languages:
        Python
        C
        JavaScript
```

### 删除空白
`'python'`和`'python '`是不一样的字符串，有时删除这样的空白意义重大
下来的实验应该在终端完成

```
>>> favorite_language = ' python '
>>> favorite_language
' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language
' python '
>>> favorite_language = favorite_language.lstrip()
>>> favorite_language
'python '
>>> favorite_language = favorite_language.strip()
>>> favorite_language
'python'
```
### 删除前缀、后缀
使用`removeprefix()`和`removesuffix()`

```
>>> url = 'https://text.org'
>>> simple_url = url.removeprefix('https://')
>>> simple_url
'text.org'
```

```
>>> filename = 'python_notes.md'
>>> simple_filename = filename.removesuffix('.md')
>>> simple_filename
'python_notes'
```

## 数

### 整数

```python
print(2+3)
print(3-2)
print(2*3)
print(3/2)  #带小数
print(3**2) #乘方运算
print(2 + 3*4)
print((2+3)*4)
```
结果
```
5
1
6
1.5
9
14
20
```

### 浮点数
一般来说，py会按照期望的方式处理

```
>>> 0.1 + 0.1
0.2
>>> 2*0.1
0.2
>>> 0.2 + 0.1
0.30000000000000004
>>> 3*0.1
0.30000000000000004
```
> 由于浮点数的表示方式，某些小数是不精确的

### 整数和浮点数

只要有操作数是浮点数，结果就是浮点数，任意两个整数相除，结果也总是浮点数

```
>>> 4/2
2.0
>>> 1 + 2.0
3.0
```

### 数中的下划线
在书写很大的数时可以用`_`分组，但是py不会打印这些下划线

```python
universe_age = 14_000_000_000
print(universe_age)
```

```
14000000000
```

### 同时给多个变量赋值

```python
x,y,z = 0,1,2
```

### 常量
py没有内置的常量类型
通常用全大写字母来指出其值应始终不变

```python
MAX_NUM = 5000
```

## 注释
在py中用`#`标识注释

```python
#一个小注释
print("hello")
```

## Python之禅
在终端打出`import this`

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

# 列表简介

列表(list)指由一系列按特定顺序排列的元素组成
在py中用`[]`来表示列表，用逗号来分隔其中的元素

```python
bicycles = ['trek','cannondale','redline']
print(bicycles)
```

```
['trek', 'cannondale', 'redline']
```
> 打印会打印列表的全部

## 访问列表元素

这与数组有相似之处，列表名称\[索引]。(索引从0开始)
```python
print(bicycles[0])
```
那么因为`bicycles[0]`是字符串，所有对字符串的操作都可以直接用
```python
print(bicycles[0].title())
```

python提供了负数索引
```python
print(bicycles[-1]) #这回打印最后一个元素
print(bicycles[-2]) #这会打印倒数第二个元素
```

### 使用列表中的各个值
可以像变量一样使用列表中的各个值

```python
message = f"My bicycle is a {bicycles[0]}."
print(message)
```

## 修改、添加和删除元素

### 修改
```python
motocycles = ['honda','yamaha','suzuki']
print(motocycles)

motocycles[0] = 'ducati'
print(motocycles)
```

```
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```

### 添加
#### 在末尾添加
使用`append()`添加
```python
motocycles.append('ducati')
print(motocycles)
```

```
['honda', 'yamaha', 'suzuki', 'ducati']
```

可以使用`append()`动态创建一个列表
```python
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')

print(motocycles)
```

#### 在列表中插入元素
使用`insert()`在任意位置添加新元素
```python
motocycles.insert(0,'ducati')
```
> 这个操作将`'ducati'`插入到索引0的位置，每个既有元素位置都后移一位

### 删除
#### 使用del语句删除元素
```python
motocycles = ['honda','yamaha','suzuki']
del motocycles[0]
print(motocycles)
```

```
['yamaha', 'suzuki']
```

#### 使用pop()方法删除元素
删除列表末尾，并可以接着使用它，列表就像一个栈，删除末尾元素就像弹出栈顶元素
```python
motocycles = ['honda','yamaha','suzuki']
print(motocycles)
poped_motocycle = motocycles.pop()
print(motocycles)
print(poped_motocycle)
```

```
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```
实际上，`pop()`也可以删除别的位置的元素，只需加上索引
```python
motocycles = ['honda','yamaha','suzuki']
print(motocycles)
poped_motocycle = motocycles.pop(1)
print(motocycles)
print(poped_motocycle)
```

```
['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']
yamaha
```

#### 根据值删除元素
索引未知的情况下，使用`remove()`方法删除
```python
motocycles = ['honda','yamaha','suzuki','ducati']
print(motocycles)
motocycles.remove('ducati')
print(motocycles)
```

```
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```
> ***`remove()`只能删除第一个指定的值，若列表中多次出现，需要使用循环来确保每个值都删除***

## 管理列表
### 使用`sort()`方法对列表进行永久排序
```python
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
```

```
['audi', 'bmw', 'subaru', 'toyota']
```
> 现在汽车是按字母顺序排序的，还可以按相反顺序排序

```python
cars.sort(reverse=True)
```

```
['toyota', 'subaru', 'bmw', 'audi']
```

#### 使用`sorted()`函数对列表进行临时排序
保留原来的顺序，并以特定的顺序来呈现它们
```python
cars = ['bmw','audi','toyota','subaru']
print("Original list:")
print(cars)
print("\nSorted list:")
print(sorted(cars))
print("\nOriginal list again:")
print(cars)
```

```
Original list:
['bmw', 'audi', 'toyota', 'subaru']

Sorted list:
['audi', 'bmw', 'subaru', 'toyota']

Original list again:
['bmw', 'audi', 'toyota', 'subaru']
```
> ***在并非所有字母都是小写的情况下时，稍复杂一点，要指定准确的排列顺序***

#### 反向打印列表
使用`reverse()`方法反转列表
```python
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
```

```
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
```

#### 确定列表的长度
使用`len()`函数可以快速获得列表长度
```
>>> cars = ['bmw','audi','toyota','subaru']
>>> len(cars)
4
```

# 操作列表

## 遍历整个列表
```python
magicians = ['alice','david','carolina']
for magician in magicians: #magician 是临时变量，通常建议使用与列表相关联的命名
    print(magician)
```

```
alice
david
carolina
```

### 在for循环中执行更多操作
在`for`循环后面的每一行缩进都是循环的一部分
```python
magicians = ['alice','david','carolina']
for magician in magicians:  #magician 是临时变量，通常建议使用与列表相关联的命名
    print(f"{magician.title()}, that is a great trick!")
    print("I can't wait to see your next trick")
```

```
Alice, that is a great trick!
I can't wait to see your next trick
David, that is a great trick!
I can't wait to see your next trick
Carolina, that is a great trick!
I can't wait to see your next trick
```

> ***python 根据缩进来判断代码行与其他部分的关系，必须注意！！！***

## 创建数值列表

### 使用`range()`函数
```python
for val in range(1,5):
    print(val)
```

```
1
2
3
4
```
> **注意：不会打印5，到达指定的第二个数是就会停止**

### 使用`range()`函数创建数值列表
可使用`list()`函数将`range()`函数的结果直接转化为列表
```python
nums = list(range(1,6))
print(nums)
```

```
[1, 2, 3, 4, 5]
```

使用`range()`函数时还可以指定步长
```python
even_nums = list(range(2,11,2))
print(even_nums)
```

```
[2, 4, 6, 8, 10]
```

还可以创建别的数值列表
```python
square_nums = []
for val in range(1,11):
    square_nums.append(val**2)
print(square_nums)
```

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### 对数值列表执行简单的统计计算
有几个函数可以快速处理
```
>>> nums = [1,2,3,7,8,9,12,23,4,5,6]
>>> min(nums)
1
>>> max(nums)
23
>>> sum(nums)
80
```

### 列表推导式
列表推导式将for循环和创建新元素的代码合并到一行，并自动追加新元素
```python
squares = [val**2 for val in range(1,11)]
print(squares)
```

```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 使用列表的一部分
### 切片(slice)
```python
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
# 没有指定第一个索引，将自动从头开始
print(players[:4])
# 同理
print(players[2:])
# 倒数后三个
print(players[-3:])
# 还可以改变步长
print(players[0:8:2])
```

```
['charles', 'martina', 'michael']
['charles', 'martina', 'michael', 'florence']
['michael', 'florence', 'eli']
['michael', 'florence', 'eli']
['charles', 'michael', 'eli']
```

### 遍历切片
```python
players = ['charles','martina','michael','florence','eli']
for player in players[:3]:
    print(player.title())
```

```
Charles
Martina
Michael
```

### 复制列表
```python
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite are:")
print(friend_foods)
```

```
My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite are:
['pizza', 'falafel', 'carrot cake']
```
**核心是使用切片来复制列表**而不是
```python
friend_foods = my_foods
```
> **这是将新变量`friend_foods`关联到`my_foods`，这两个将始终相同**

## 元组
不可变的列表称为元组(tuple)
### 定义元组
使用`()`来标识
```python
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
```

```
200
50
```

假如修改元组的值
```python
dimensions[0] = 250
```

```
Traceback (most recent call last):
  File "e:\learn\Python_learning\dimensions.py", line 4, in <module>
    dimensions[0] = 250
    ~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

> ***注意：严格来说，元组是由`,`标识的，如果只定义一个只包含一个元素的元组，必须在这个元素后面加上逗号***

### 遍历元组中的所有值
```python
for dimension in dimensions:
    print(dimension)
```

### 修改元组变量
可以给元组整个重新赋值
```python
dimensions = (200,50)
print("Original tuple:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nModified tuple:")
for dimension in dimensions:
    print(dimension)
```

```
Original tuple:
200
50

Modified tuple:
400
100
```

# 设置代码格式(PEP8)
PEP8 是 Python Enhancement Proposal 8 的缩写，它是 Python 官方推荐的**代码风格指南**，核心目的是让所有Python开发者的代码风格保持一致，提升代码的可读性和维护性。
#### 1. 缩进（最基础也最重要）
- 必须使用 **4个空格** 作为一个缩进级别，**禁止使用Tab**（如果编辑器混用了Tab和空格，会报语法错误）；
- 换行后的续行，缩进要比上一行多4个空格，或对齐到括号/等号的位置：
  ```python
  # 正确
  total = (first_num
           + second_num
           - third_num)
  
  # 正确（续行缩进4个空格）
  def calculate(a, b, c):
      return a * b + \
          c / 2
  ```

#### 2. 行长度
- 一行代码的字符数**不超过79个**（注释行不超过72个），过长时拆分成多行，提升可读性；
- 例外：URL、长字符串常量、命令行指令等可适当放宽，但尽量遵循。

#### 3. 空行
- 函数/类之间用 **2个空行** 分隔；
- 函数内部的逻辑块之间用 **1个空行** 分隔，区分不同功能：
  ```python
  def func1():
      pass
  
  
  def func2():
      # 逻辑块1
      a = 1
      b = 2
      
      # 逻辑块2（空行分隔）
      c = a + b
      return c
  ```

#### 4. 空格使用规范
- 运算符（`+`、`=`、`*` 等）两侧加1个空格，**括号内侧不加空格**：
  ```python
  # 正确
  x = 10 + 20 * (30 - 5)
  if (x > 0) and (y < 10):
      pass
  
  # 错误
  x=10+20*(30-5)  # 运算符无空格
  if ( x > 0 ) and ( y < 10 ):  # 括号内侧加了空格
      pass
  ```
- 逗号、分号后加1个空格，前面不加：
  ```python
  # 正确
  fruits = ['apple', 'banana', 'orange']
  for i in range(1, 10):
      pass
  ```

#### 5. 命名规范
这是新手最容易混乱的点，PEP8明确了不同对象的命名规则：

| 类型         | 命名方式       | 示例               |
|--------------|----------------|--------------------|
| 变量/函数    | 小写+下划线    | `user_name`、`get_score()` |
| 常量         | 大写+下划线    | `MAX_SIZE`、`PI = 3.14159` |
| 类           | 大驼峰（首字母大写） | `Student`、`UserInfo` |

#### 6. 导入规范
- 导入语句放在文件顶部，按“标准库→第三方库→自定义模块”的顺序，每组之间用空行分隔；
- 禁止一行导入多个模块，优先使用绝对导入：
  ```python
  # 正确
  import os
  import sys
  
  import requests
  import pandas as pd
  
  from my_project import utils
  ```

#### 7. 注释
- 单行注释用 `#`，且 `#` 后加1个空格；
- 注释要简洁、准确，只注释“为什么这么做”，而非“做了什么”（代码本身能看懂的逻辑无需注释）：
  ```python
  # 错误（废话注释）
  # 给x赋值10
  x = 10
  
  # 正确（解释原因）
  # 初始值设为10，兼容老版本接口的默认参数
  x = 10
  ```

# `if`语句
## 条件测试
### 检查是否相等
使用相等运算符`==`
```
>>> car = 'bmw'
>>> car == 'bmw'
True
>>> car == 'audi'
False
```
在检查相等时，忽略大小写
```
>>> car = 'Audi'
>>> car == 'audi'
False
>>> car.lower() == 'audi'
True
```
### 检查是否不等
使用`!=`
```python
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

```
Hold the anchovies!
```

### 数值比较
```
>>> age = 19
>>> age == 19
True
>>> age != 9
True
>>> age > 8
True
>>> age >= 20
False
>>> age <= 19
True
```

### 检查多个条件
#### 1.使用`and`检查多个条件
```
>>> age_0 >= 21 and age_1 >= 21
False
>>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
```
#### 2.使用`or`检查多个条件
```
>>> age_0 = 22
>>> age_1 = 18
>>> age_0 >= 21 or age_1 >= 21
True
>>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
```

### 检查特定的值是否在列表中
使用`in`
```
>>> requested_topping = ['mushrooms','onions','pineapple']
>>> 'mushrooms' in requested_topping
True
>>> 'pepperoni' in requested_topping
False
```
那么是否不在就使用`not in`
```python
banned_users = ['andrew','carolina','david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")
```

```
Marie,you can post a response if you wish.
```

### 布尔表达式
在跟踪程序状态或程序中重要的条件方面，布尔值提供了一种高效的方式
```python
game_active = True
can_edit = False
```
> **首字母大写哦**

## `if`语句
`if`语句和`if-else`语句都是很简单的，skip
### `if-elif-else`
```python
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
```

为了让程序更简洁,可以统一出口
```python
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}")
```
可以使用多个`elif`，也可以省略`else`

### 测试多个条件
这需要多个独立的`if`语句。而不是使用`if-elif-else`语句（这会导致，只要有一个成立，余下的不会执行）
```python
requested_topping = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")

print("\nFinished making your pizza.")
```

## 使用`if`语句处理列表
### 检查特殊元素
```python
requested_topping = ['mushrooms','onions','pineapple']
if 'mushrooms' in requested_topping:
    print("Adding mushrooms")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni")  

print("\nFinished making your pizza.")
```

```
Adding mushrooms
Adding onions
Adding pineapple
Sorry, we are out of green peppers.

Finished making your pizza!
```
### 确定列表非空
```python
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        if topping == 'green peppers':
            print("Sorry, we are out of green peppers.")
        else:
            print(f"Adding {topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

```
Are you sure you want a plain pizza?
```

### 使用多个列表
```python
available_toppings = ['mushrooms','onions','pineapple',
                      'pepperoni','olives','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")
print("\nFinished making your pizza.")
```

```
Adding mushrooms
Sorry, we don't have french fries
Adding extra cheese

Finished making your pizza.
```

# 字典
## 一个简单的字典
```python
alien_0 = {'color': 'green','points': 5}

print(alien_0['color'])
print(alien_0['points'])
```

```
green
5
```

## 使用字典
字典是一系列的键值对，每个键与一个值相关联
### 访问字典中的值
想上面那样
```python
new_points = alien_0['points']
```
### 添加键值对
```python
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
```

```
{'color': 'green', 'points': 5, 'x_pos': 0, 'y_pos': 25}
```

### 从创建一个空字典开始
存储大量数据或编写自动生成键值对的代码通常需要定义一个空字典
### 修改字典中的值
```python
alien_0 = {'x_pos': 0,'y_pos': 25,'speed': 'medium'}
print(f"Original pos: {alien_0['x_pos']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 移动速度非常快
    x_increment = 3

alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(f"Now pos: {alien_0['x_pos']}")
```

```
Original pos: 0
Now pos: 2
```
### 删除键值对
使用`del`删除
```python
del alien_0['color']
print(alien_0)
```

```
{'color': 'green', 'points': 5, 'x_pos': 0, 'y_pos': 25}
{'points': 5, 'x_pos': 0, 'y_pos': 25}
```

### 由类似的对象组成的字典
```python
favorite_language = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Java',
    'phil': 'Rust'
}

print(f"Sarah's favorite language is {favorite_language['sarah']}")
```

```
Sarah's favorite language is C
```

### 使用`get()`来访问值
使用方括号有时会产生问题，如果指定的key不存在，就会出错
```python
point_val = alien_0.get('points','No point val assigned.')
print(point_val)
```

`get(查询的key，指定的key不存在时返回的值)`
> 如果没有指定第二个参数，默认返回`None`

## 遍历字典
### 遍历所有键值对`items()`方法
```python
user_0 = {
    'username': 'efe',
    'first': 'enrico',
    'last': 'fermi'
}

for key,val in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nVal: {val}")
```

```
Key: username

Val: efe

Key: first

Val: enrico

Key: last

Val: fermi
```
### 遍历所有键`keys()`方法
```python
for name in favorite_language.keys():
    print(name.title())
```

```
Jen
Sarah
Edward
Phil
```

### 按特定顺序遍历字典中的所有键
```python
for name in sorted(favorite_language.keys()):
    print(name.title())
```

```
Edward
Jen
Phil
Sarah
```

### 遍历字典中所有值`values()`方法
```python
for language in favorite_language.values():
    print(language)
```

```
Python
C
Java
Rust
```
> **这种方法应对数据量较小时没有问题，但是有大量重复元素时，需剔除重复项**

可以使用`set()`集合来处理
```python
favorite_language = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Java',
    'phil': 'Python'
}
for language in set(favorite_language.values()):
    print(language)
```

```
Java
Python
C
```
> **集合是无序的，每次顺序可能不一样，但是元素一定唯一。可以直接用`{}`定义一个集合**

```python
languages = {'python','java','rust'}
```

## 嵌套
### 字典列表
```python
# 创建一个用于存储外星人的空列表
aliens = []
for alien_num in range(30):
    new_alien = {'color': 'green','points': 5}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total num of aliens: {len(aliens)}")
```

```
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5}
...
Total num of aliens: 30
```

### 在字典中存储列表
```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
```

```
You ordered a thick-crust pizzawith the following toppings:
        mushrooms
        extra cheese
```

```python
favorite_languages = {
    'jen': ['Python','Rust'],
    'sarah': ['C'],
    'edward': ['Java','Go'],
    'phil': ['Python','haskell'],
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language}")
```

```
Jen's favorite languages are:
        Python
        Rust

Sarah's favorite languages are:
        C

Edward's favorite languages are:
        Java
        Go

Phil's favorite languages are:
        Python
        haskell
```

### 在字典中存储字典
```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

```
Username: aeinstein
        Full name: Albert Einstein
        Location: Princeton

Username: mcurie
        Full name: Marie Curie
        Location: Paris
```

# 用户输入和`while`循环
## `input()`函数的工作原理

```python
message = input("Tell me someing, and I will repeat it back to you:")
print(message)
```

```
Tell me someing, and I will repeat it back to you:hello
hello
```
> **`input()`函数接受一个参数，是向用户显示的提示，用户的输入会赋给变量**

### 编写清晰的提示
有时提示会超过一行，可以先将prompt赋给变量，再用变量传参
```python
prompt = "If you share your name, we can personalize the message you see"
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello {name}")
```

```
If you share your name, we can personalize the message you see
What is your first name?Jack

Hello Jack
```

### 使用`int()`来获取数值输入
使用`input()`函数获取数值时，解释器会将其解释为字符(串)。

```python
height = input("How tall are you, in inches?")
height = int(height)
if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

```
How tall are you, in inches?71

You are tall enough to ride!
```

### 求模运算符

这与其他语言中的`%`并无不同
```
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
```

## `while`循环简介
### 使用`while`循环
```python
curr_num = 1
while curr_num <= 5:
    print(curr_num)
    curr_num += 1
```

```
1
2
3
4
5
```

### 使用标志来退出程序
```python
prompt = "\nTell me someing, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

```
Tell me someing, and I will repeat it back to you: 
Enter 'quit' to end the program.Jack
Jack

Tell me someing, and I will repeat it back to you: 
Enter 'quit' to end the program.Hell
Hell

Tell me someing, and I will repeat it back to you: 
Enter 'quit' to end the program.quit
```

### 循环控制语句
像其他语言一样，也有`break`和`continue`两种控制语句

## 使用`while`循环处理列表和字典
### 在列表之间移动元素

```python
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    curr_user = unconfirmed_users.pop()
    print(f"Verifying user: {curr_user.title()}")
    confirmed_users.append(curr_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

```
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

### 删除列表中特定值的所有元素

```python
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)
```

```
['dog', 'dog', 'goldfish', 'rabbit']
```

### 使用用户输入填充字典

```python
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Result ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")
```

```
What is your name?Jack
Which mountain would you like to climb someday?Que
Would you like to let another person respond? (yes/no)yes

What is your name?Ly
Which mountain would you like to climb someday?Mu
Would you like to let another person respond? (yes/no)no

--- Poll Result ---
Jack would like to climb Que
Ly would like to climb Mu
```

# 第八章 函数
## 8.1 定义函数
```python
def greet_user():
    """显示简单的问候语"""
    print("Hello!")
    
greet_user()
```
> **第二行文本是被称为文档字符串的注释，这些字符串通常用`""" """`引起，能够包含多行**

### 向函数传递信息
```python
def greet_user(username):
    """显示简单的问候语"""
    print(f"Hello, {username.title()}!")
    
greet_user('jesse')
```

```
Hello, Jesse!
```

稍作修改即可传递参数，与其他语言并无区别，`username`是一个形参，`'jesse'`是一个实参

## 8.2 传递实参
### 8.2.1 位置实参
基于实参的顺序进行关联
```python
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster','harry')
```

```
I have a hamster
My hamster's name is Harry.
```

> **可以多次调用函数，实际上函数就是因为会多次调用，写成函数更方便点，注意实参的顺序**

### 8.2.2 关键字实参
是传递给函数名值对(name-value pair)
```python
describe_pet(pet_name = 'harry', animal_type = 'hamster')
```
顺序不重要

### 8.2.3 默认值
```python
def describe_pet(pet_name, animal_type = 'dog'):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('whllie')
```
> **注意：使用默认值时，必须在形参列表先列出没有默认值的形参，再列出有默认值的形参**

实际上，这三种是混合使用的，只要合法等效均可

## 8.3 返回值
通过`return`语句返回值
有时可以实现实参为空的情况
```python
def get_formatted_name(first_name, last_name, middle_name = ''):
    """返回标准格式的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
cook = get_formatted_name('jimi', 'hendrix')
print(cook)
cook = get_formatted_name('jimi', 'hendrix', 'lee')
print(cook)
```

```
Jimi Hendrix
Jimi Lee Hendrix
```
实际上可以返回任何值，数据结构，比如字典，列表
```python
def build_person(first_name, last_name, age = None):
    """返回一个字典，其中包含一个的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age;
    return person

cook = build_person('jimi', 'hendrix', 27)
print(cook)
```

```
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
```

### 结合使用`while`
```python
def get_formatted_name(first_name, last_name, middle_name = ''):
    """返回标准格式的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print(f"\nHello {formatted_name}!")
```

```
Please tell me your name:
(enter 'q' at any time to quit)
First name:jimi
Last name:hed

Hello Jimi Hed!

Please tell me your name:
(enter 'q' at any time to quit)
First name:q
```

## 8.4 传递列表
我们可以实现在函数中修改列表
```python
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，
    打印每个设计后，将其移动到列表completed_models
    """
    while unprinted_designs:
        curr_design = unprinted_designs.pop()
        print(f"Printing model: {curr_design}")
        completed_models.append(curr_design)
        
def show_completed_models(completed_models):
    """显示打印好的模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone', 'robot', 'dog']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

```
Printing model: dog
Printing model: robot
Printing model: phone

The following models have been printed:
dog
robot
phone
```

可以通过向函数传递列表副本来防止函数修改列表
```python
function_name(list_name[:])
```

## 传递任意数量的实参
```python
def make_pizza(*toppings):
    """概述要制作的披萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza('mushroom')
make_pizza('pep','mushroom','cheese')
```

```
Making a pizza with the following toppings:
- mushroom

Making a pizza with the following toppings:
- pep
- mushroom
- cheese
```
> **`*`是让py创建一个名为`toppings`的元组，如果直接打印，会以元组形式出现**

### 使用任意数量的关键字实参
```python
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','einstein',
                             location = 'princeton',
                             field = 'physics')
print(user_profile)
```

```
{'location': 'princeton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
```
> **`**`是让py创建一个名为`user_info`的字典，传参是传入键值对

## 8.6 将函数存储在模块中
### 导入整个模块
模块是扩展名为`.py`的文件
```python
import pizza03

pizza03.make_pizza('mushroom')
```

```
Making a pizza with the following toppings:
- mushroom
```

### 导入特定的函数
```python
from module_name import function_0,function_1
```

### 使用`as`给模块指定别名
```python
import pizza03 as p 

p.make_pizza('mushroom')
```

也可以给函数指定别名
```python
from module_name import function_name as fn
```

### 导入模块中的所有函数

```python
from pizza import *
```
> ***注意：这是让Python将模块中的所有函数都复制到这个程序文件中，这样无须使用点号来调用程序，但是不建议这样做，在编写大型程序师可能会产生一些问题***

### 编写指南
- 在给形参指定默认值时，等号两边不要有空格
- 函数调用中的关键字实参也应该循序这种约定

# 第九章 类
***OOP是最有效的软件编写方法之一***

## 9.1 创建和使用类
```python
class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性 name 和 age"""
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")
```

根据约定，在Python中首字母大写的名称指的是类（此处是全新的类，定义时不加括号）
### `__init__()`方法
类中的函数称为方法
- `self`必不可少，Python会自动传入这个实参
- 以`self`为前缀的变量可以供类中的所有方法使用，可以通过类的所有实例访问（这种叫做属性(attribute))

### 根据类创建实例
```python
class Dog:
	--snip--
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

#### 1.访问属性
访问实例的属性可使用`.`
#### 2.调用方法
```python
class Dog:
	--snip--
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()
```

#### 3.创建多个实例
可以根据需求创建多个实例

## 9.2 使用类和实例
### Car类
```python
class Car:
    """一次模拟汽车的尝试"""
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """返回规范化的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
```
### 给属性指定默认值
有些属性可以直接在`__init__()`中指定默认值
```python
class Car:
    """一次模拟汽车的尝试"""
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回规范化的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it")
        
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

```
2024 Audi A4
This car has 0 miles on it
```

### 修改属性的值
#### 1.直接修改
通过实例访问它修改
```python
class Car:
	--snip--
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

#### 2.通过方法修改属性的值
```python
class Car:
	--snip--
	def update_odometer(self,mileage):
        """将里程表读数更新为指定的值"""
        self.odometer_reading = mileage
        
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()
```

#### 3.通过方法让属性的值递增
实际上，很多情况下，是让属性的值增加一个特定的值，而不是更新为一个新的值
```python
class Car
	--snip--
	def increment_odometer(self,miles):
        """让里程表增加特定的值"""
        self.odometer_reading += miles
```

## 9.3 继承
编写类时，并非总是从头开始，如果要编写的类是一个既有类的特殊版本，可使用继承，原有类称为父类，新类称为子类。
```python
class Car:
    """一次模拟汽车的尝试"""
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回规范化的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it")
    def update_odometer(self,mileage):
        """将里程表读数更新为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """让里程表增加特定的值"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)

my_model_y = ElectricCar('Tesla', 'model_y', 2024)
print(my_model_y.get_descriptive_name())
```

- `super()`是一个特殊的函数，让我们可以调用父类的方法
- 父类也称为超类(superclass)，`super()`因此得名

### 给子类定义属性和方法
```python
class Car
	--snip--
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        先初始化父类的属性，
        再初始化特有属性
        """
        super().__init__(make, model, year)
        self.battery_size = 40
    def describe_battery(self):
        """打印一条电池容量信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_model_y = ElectricCar('Tesla', 'model_y', 2024)
print(my_model_y.get_descriptive_name())
my_model_y.describe_battery()
```

```
2024 Tesla Model_Y
This car has a 40-kWh battery.
```

### 重写父类中的方法
```python
class ElectricCar(Car):
	-- snip --
	def fill_gas_tank(self):
        """电动汽车没油油箱"""
        print("This car doesn't have a gas tank.")
```

假设`Car`类中有`fill_gas_tank()`这个方法，现在Python将忽略父类中的这个方法，转而运行上述代码

### 将实例用作属性
将大型类拆分成多个协同工作的小类，这种方法称为组合
```python
class Car
	--snip--
class Battery:
    """一次模拟电动汽车电池的简单尝试"""
    def __init__(self, battery_size=40):
        """初始化电池属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条电池容量信息"""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        先初始化父类的属性，
        再初始化特有属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """电动汽车没油油箱"""
        print("This car doesn't have a gas tank.")


my_model_y = ElectricCar('Tesla', 'model_y', 2024)
print(my_model_y.get_descriptive_name())
my_model_y.battery.describe_battery()
```

## 9.4 导入类
### 导入单个类，在一个模块中存储多个类
```python
from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

```
2024 Ford Mustang
2024 Nissan Leaf
```

### 导入整个模块
- 这与函数相同，导入整个模块后，需要使用`.`
- 当然，也可以在一个模块中导入另一个模块

### 导入模块的所有类
```python
from module_name import *
```
> **依然不推荐这种方法**

### 使用别名
可以给模块中的类，或者模块指定别名
## 9.5 Python 标准库
下面示范一个
```
>>> from random import randint
>>> randint(1, 6)
1
```

```
>>> from random import choice
>>> players = ['cah', 'jie', 'loo']
>>> first_up = choice(players)
>>> first_up
'cah'
```

> ***在创建与安全有关的项目时，不要使用`random`模块，此外，还可以导入很多外部模块***

## 9.6 类的编程风格
- 类名应采用大驼峰式命名法
	- `ElectricCar`
- 每个类，都应在类定义后面紧跟一个文档字符串
- 先写标准库模块中的`import`语句，再写自己的模块

# 第十章 文件和异常

## 10.1 读取文件
### 10.1.1 读取文件的全部内容
```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
```

```
3.1415926535
   8979323846
   2643383279
   
```

>**理论上，结尾会出现一个空行，`read_text()`在到达文件末尾时会返回一个空字符串，此时可以使用`rstrip()`**

### 10.1.2 文件的相对路径和绝对路径
- 最简单的做法就是把文件和程序文件放在同一个文件夹中（且不在子文件夹中）
- 当然最稳妥的做法是使用绝对路径

> **在显示文件路径时，win会使用`\`而不是`/`，但在代码中应该始终使用`/`，`pathlib`库会自动使用正确的路径表示方法**

### 10.1.3 访问文件中的各行
- 可以使用`splitlines()`方法将冗长的字符串转换成一系列的行，再使用`for`循环每次一行来检查
```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
for line in lines:
    print(line)
```
- `splitlines()`返回一个列表，包含文件中的所有行

### 10.1.4 使用文件的内容
```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line
    
print(pi_string)
print(len(pi_string))
```

```
3.1415926535   8979323846   2643383279
38
```

```python
for line in lines:
    pi_string += line.lstrip()
```

```
3.141592653589793238462643383279
32
```
> ***注意：读取文件时，所有内容都是字符串，如要以数值形式理解，需使用`int()`，`float()`转换***

### 10.1.5 包含100万位的大型文件
```python
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))
```

```
3.14159265358979323846264338327950288419716939937510...
1000002
```

```python
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
 
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

```
Enter your birthday, in the form mmddyy: 051407
Your birthday does not appear in the first million digits of pi.
```

## 10.2 写入文件
### 10.2.1 写入一行
```python
from pathlib import Path

path = Path('programming.txt')
path.write_text("Python is fun!")
```

>**Python只能将字符串写入文本文件，数值数据需先使用`str()`转换

### 10.2.2 写入多行
```python
from pathlib import Path

contents = "hello.\n"
contents += "greetings.\n"
contents += "superise.\n"

path = Path('programming.txt')
path.write_text(contents)
```
> **使用`write_text()`时，需要谨慎，如果指定文件已经存在，它会先删除其内容，并将指定内容写入其中**

## 10.3 异常
- Python使用称为异常(exception)的特殊对象来管理程序执行期间的错误
- 每当发生错误，都会创建一个异常对象
- 如果编写了处理该异常的代码，程序就会继续运行
- 如果没有处理，程序将停止，并显示一个`traceback`

### 10.3.1 `ZeroDivisionError`异常（除0错误）
```python
>>> print(5/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

### 10.3.2 使用`try-except`代码块
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

```
You can't divide by zero!
```

### 10.3.3 使用异常避免崩溃和`else`代码块
```python
print("Give you two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("Second number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
```

```
Give you two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 8
Second number: 4
2.0

First number: 9
Second number: 0
You can't divide by zero!

First number: q
```
> **成功执行`try`代码块的运算后，就会执行`else`代码块中的代码**

### 10.3.4 处理`FileNotFoundError`异常
```python
from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')
```
> ***注意：如果系统默认编码与要读取的文件的编码不一致，参数`encoding`必不可少

```python
Traceback (most recent call last):
  File "e:\learn\Python_learning\CCF_ComputerDesign\yuhaolin\file_io\alice.py", line 4, in <module>
    contents = path.read_text(encoding='utf-8')
  File "C:\Users\36259\AppData\Local\Programs\Python\Python313\Lib\pathlib\_local.py", line 546, in read_text
    return PathBase.read_text(self, encoding, errors, newline)     
           ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     
  File "C:\Users\36259\AppData\Local\Programs\Python\Python313\Lib\pathlib\_abc.py", line 632, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors, newline=newline) as f:
         ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\36259\AppData\Local\Programs\Python\Python313\Lib\pathlib\_local.py", line 537, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```
> **重点关注最后一行，和第一处`line 4`，要将错误代码行放入`try`中，并编写对应的`except`**

```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("The file 'alice.txt' was not found.")
```

```
The file 'alice.txt' was not found.
```

### 10.3.5 分析文本
```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("The file 'alice.txt' was not found.")
else:
    words = contents.split()
    num_words = len(words)
    print(f"The file 'alice.txt' has about {num_words} words.")
```

```
The file 'alice.txt' has about 29594 words.
```

> **使用`split()`方法，以空白为分隔符将字符串分拆为多个部分**

### 10.3.6 静默失败  
```python

```