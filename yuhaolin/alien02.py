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
