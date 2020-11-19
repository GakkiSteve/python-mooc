alist = list(map(int,input().split()))
length = len(alist)
mid = length//2
mydict = {'1':alist[:mid],'2':alist[mid:]}
print(mydict)