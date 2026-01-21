favorite_language = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Java',
    'phil': 'Rust'
}

print(f"Sarah's favorite language is {favorite_language['sarah']}")

for name in favorite_language.keys():
    print(name.title())

for name in sorted(favorite_language.keys()):
    print(name.title())

for language in favorite_language.values():
    print(language)
    
favorite_language = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Java',
    'phil': 'Python'
}
for language in set(favorite_language.values()):
    print(language)