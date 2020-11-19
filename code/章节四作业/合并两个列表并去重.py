alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
clist = sorted(list(set(alist + blist)))
print(clist)