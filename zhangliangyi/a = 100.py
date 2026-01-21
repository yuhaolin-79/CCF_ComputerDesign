str1  = '三点水'
print(str1)

str2 = "三'点'水"
print(str2)

str3 = '两\'点\'水'
print(str3)

str4  = '''三
点
水'''
print(str4)

str5 = 4/2
print(type(str5))

str6 = 4**2
print(str6)

print(int (88.88))


a,b,c = 1 , 87.45 , 'zhangsan'
print(a,b,c)

name = 'zhangsan'
name1 = f'hello, {name}.\nwelcome'
name2 = 'hello,{}.\nwelcome'.format(name)
print(name1)
print(name2)

name3 = ['(zhangsan).\n', 'lisi.\n', 15.55]
print(name3)

name = ['一点水', '两点水', '三点水', '四点水', '五点水吗ass']
print(name[2])
print(name[0:2])

name.append('六点水')
print(name)

del name[2]
print(name)

num = len(name)
print(num)

name1 = [4 , 5 , 5 , 6, 6]
name = name + name1
print(name)
num = len(name)
print(num)
name3 = name[3] * 2 

print(name3)
num = len(name3)
print(num)

print(3 in name)
ass = 3 in name
print(ass)




