from name_function import get_formatted_name

def test_name_function():
    """能正确处理像 'janis joplin' 这样的姓名吗？"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
    
def test_first_last_middle_name():
    """能正确处理像 'wolfgang amadeus mozart' 这样的姓名吗？"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'