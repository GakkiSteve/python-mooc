def fac(n):
    mylist = []
    for i in range(1,n):
        if n % i == 0:
            mylist.append(i)
    return mylist

n = int(input())
for i in range(2, n+1):
    mylist = fac(i)
    mysumm = 0
    for j in mylist:
        mysumm += j
    if mysumm == i:
        print(mysumm)