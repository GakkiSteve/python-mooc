def test(i,j,k):
    if i + j > k and i + k > j and j + k > i \
    and i - j < k and i - k < j and j - k < i:
        return True
    else:
        return False



mylist = list(map(int,input().split()))
length = len(mylist)
maxx = 0
if length < 3:
    print(0)
else:
    for i in range(length):
        for j in range(length):
            for k in range(length):
                #print("ijk",i,j,k)
                #print("value",mylist[i],mylist[j],mylist[k])
                if test(mylist[i],mylist[j],mylist[k]) and i != j and i != k and j != k:
                    if mylist[i] + mylist[j] + mylist[k] > maxx:
                        maxx = mylist[i] + mylist[j] + mylist[k]
            
print(maxx)