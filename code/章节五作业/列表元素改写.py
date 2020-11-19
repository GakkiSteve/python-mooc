mylist = list(map(int,input().split()))
ans = []
for i in mylist:
    if i % 2 == 0:
        ans.append(i//2)
    else:
       ans.append(i**2)
print(sorted(ans))