def add_binary(a,b):
    return bin(a+b)[2:]

print(add_binary(1,1),
      add_binary(0,1),
      add_binary(1,0),
      add_binary(51,12))