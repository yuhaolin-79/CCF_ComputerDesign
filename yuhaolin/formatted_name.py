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