def bubbleSort(alist):
    length = len(alist) - 1
    for i in range(length):
        for j in range(length - i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1],alist[j]
    return alist
    
    
    
alist=list(map(int,input().split()))
print(bubbleSort(alist))