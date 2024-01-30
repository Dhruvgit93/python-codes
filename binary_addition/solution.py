def add_binary(a,b):
    return bin(a+b)[2:]
s='-1 2 3 4 -5'
print(min([int(x) for x in s.split()]))

print(add_binary(1,1),
      add_binary(0,1),
      add_binary(1,0),
      add_binary(51,12))