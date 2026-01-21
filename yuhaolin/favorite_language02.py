favorite_languages = {
    'jen': ['Python','Rust'],
    'sarah': ['C'],
    'edward': ['Java','Go'],
    'phil': ['Python','haskell'],
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language}")
        
