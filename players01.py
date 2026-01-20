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