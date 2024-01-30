def high_and_low(numbers):
    lt=[int(x) for x in numbers.split()]
    return f'{max(lt)} {min(lt)}'

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
      ,high_and_low("1 2 3"))