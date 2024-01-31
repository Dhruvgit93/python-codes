ls=[0,1]
def fabonacci(upto):
    for x in range(0,upto):
        ls.append(ls[x]+ls[x+1])
    return print(sum(ls),ls)    
        
fabonacci(7)