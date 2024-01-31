def perimeter(n):
    ls=[0,1]
    for x in range(0,n):
        ls.append(ls[x]+ls[x+1])
    return sum(ls)*4

print(perimeter(5)==80,
      perimeter(7)==216)