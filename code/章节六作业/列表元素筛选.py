def foo(alist):
    mylist = []
    length = len(alist)
    for i in range(1, length, 2):
        mylist.append(alist[i])
    return mylist
        
    
    
alist=list(map(int,input().split()))
print(foo(alist))