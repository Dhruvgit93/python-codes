def descending_order(num):
    # l=[int(x) for x in str(num)]
    # l.sort(reverse=True)
    # return int(''.join(map(str,l)))

    return int(''.join(sorted(str(num))[::-1]))

print(descending_order(0)==0,
      descending_order(15)==51,
      descending_order(92929)==99922)