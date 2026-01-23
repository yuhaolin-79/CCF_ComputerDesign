def build_person(first_name, last_name, age = None):
    """返回一个字典，其中包含一个的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age;
    return person

cook = build_person('jimi', 'hendrix', 27)
print(cook)