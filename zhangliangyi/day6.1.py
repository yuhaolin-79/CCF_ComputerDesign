#chr ASCLL方式
fp = open('note.txt', 'w')
print("北京欢迎你", file=fp)
fp.close()

print("北京欢迎你"+"10086")


# num = input("请输入")
# num = int(num)
# print(num)

# while True:
#     try:
#         num = int(input("请输入"))
#         print(f'你输入的数字是{num}')
#         break
#     except ValueError:
#         print("输入无效，请重新输入")

# num = int(input("请输入"))
# print(num)

no = number = 1024
print(no,number)
print(id(no))
print(id(number))

num1 = 987
num2 = 0b1111011011
num3 = 0o1733
num4 = 0x3DB
print(num1, num2, num3, num4)


x=199E46
print(x)
print(type(x))

x = 531+46j
print(x.real)
print(x.imag)
print("北京欢迎你"[4])
print(ord("你"))

#True = 1
#False = 0
#bool 用来测量布尔值
#非0 的布尔值都为True 1
#所有非空字符串的值都为True

print(int('10086')+int('5201314'))
print(ord('杨'))
print(chr(20320))
print(hex(255))
print(oct(255))
print(bin(255))


s= "3+3.14"
print(type(s))
s1 = eval(s)
print(type(s1))

# height = eval(input("请输入身高（米）："))
# print(height,type(height))

print(not False)

#  &  |   ^   ~  

#<<

score = input("请输入成绩等级：")
match score:
    case 'A':
        print("优秀")
    case 'B':
        print("良好")
    case 'C':
        print("及格")

#for 循环变量 in 遍历序列:
sum = 0
for i in range(1,11):
  sum +=i
  if i ==   10:
    print(sum)
    s =0 
    for i in range(1,11):
     s+= i   
    else:
            print(s)


    answer = input("今天要上课吗？")
    while answer  == 'y':
        print("好好学习，天天向上")
        answer = input("今天要上课吗？")
    else:
        print("不学习，回家睡觉")


i = 0
while i < 3:
    a = input("请输入用户名：")
    b = input("请输入密码：")
    if a == 'admin' and b == '123456':
        print("登录成功")
        break
    else:
        if i < 2:
            print ('用户名或密码错误，还有',2-i,'次机会，请重新输入')
        i += 1
        if i== 3:
            print("登录失败，账户已锁定，请联系管理员")

