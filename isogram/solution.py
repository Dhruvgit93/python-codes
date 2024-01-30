def is_isogram(string):
    check=[]
    for letter in string.lower():
        if letter in check:
            return False
        else:
            check.append(letter)
    return True
    
print(is_isogram("Dermatoglyphics"),
is_isogram("aba"),
is_isogram(""))
