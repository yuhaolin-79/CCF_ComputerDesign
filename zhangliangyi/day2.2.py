set1=set([123,456,789])
print(set1)

set1=set([123,456,789])
print(set1)
set1.remove(456)
print(set1)

#warning
set1=set('hello')
set2=set(['p','y','y','h','o','n'])
print(set1)
print(set2)

set1=set('hello')
set2=set(['p','y','y','h','o','n'])
print(set1)
print(set2)

# 交集 (求两个 set 集合中相同的元素)
set3=set1 & set2
print('\n交集 set3:')
print(set3)
# 并集 （合并两个 set 集合的元素并去除重复的值）
set4=set1 | set2
print('\n并集 set4:')
print(set4)
# 差集
set5=set1 - set2
set6=set2 - set1
print('\n差集 set5:')
print(set5)
print('\n差集 set6:')
print( set6)


# 去除海量列表里重复元素，用 hash 来解决也行，只不过感觉在性能上不是很高，用 set 解决还是很不错的
list1 = [111,222,333,444,111,222,333,444,555,666]  
set7=set(list1)
print('\n去除列表里重复元素 set7:')
print(set7)

# -*-coding:utf-8-*-

results = 89

if results > 90:
    print('优秀')
elif results > 80:
    print('良好')
elif results > 60:
    print ('及格')
else :
    print ('不及格')


if results >= 60 and  results <90 and results !=80:
    print("666,演都不演了")

for letter in 'Hello 两点水':
    print(letter)

dict = {'1':'zhangsan','2':'lisi','3':'wangwu'}
for i in dict:
    print(i,dict[i]) 
    print(i)   

#比如，你试了之后，会发现整数和浮点数是不可以直接放在 for 循环里面的。

for i in range(3):
    print(i)

for i in range(3,9,3):
    print(i)


for i in range(0, 10):
    print(i)


i = 0
while i < 10:
    print(i)
    i = i + 1

count = 1
sum = 0
while (count <= 100):
    sum = sum + count
    if ( sum > 1000):  #当 sum 大于 1000 的时候退出循环
        break
    count = count + 1
print(sum)


for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 是一个合数' % num)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print ('%d 是一个质数' % num)




