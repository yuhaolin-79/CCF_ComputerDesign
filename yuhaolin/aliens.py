# 创建一个用于存储外星人的空列表
aliens = []
for alien_num in range(30):
    new_alien = {'color': 'green','points': 5}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total num of aliens: {len(aliens)}")
