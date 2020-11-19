alist = list(map(int,input().split()))
alist.sort(key = abs)
print(alist)