alien_0 = {'color': 'green','points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)

del alien_0['points']
print(alien_0)

point_val = alien_0.get('points','No point val assigned.')
print(point_val)