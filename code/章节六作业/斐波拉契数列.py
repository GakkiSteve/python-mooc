def fbnq(n):
    mylist = [1,1]
    if n < 2:
        return mylist[n-1]
    else:
        while len(mylist) != n:
            mylist.append(mylist[-1]+mylist[-2])
        else:
            return mylist[-1]


n=int(input(""))
print(fbnq(n))