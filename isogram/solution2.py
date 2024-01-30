def is_isogram(string):
    return len(set(string.lower()))==len(string)
    
print(is_isogram("Dermatoglyphics"),
is_isogram("aba"),
is_isogram(""))
