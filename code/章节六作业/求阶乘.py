def fact(n):
    summ = n
    tmp = n-1
    while tmp != 0:
        summ *= tmp
        tmp -= 1
    return summ
    
    