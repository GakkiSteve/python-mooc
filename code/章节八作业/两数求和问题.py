mylist = list(map(int,input().split()))
target = int(input())
length = len(mylist)
ans = []
flag = 0
for i in range(length):
    for j in range(length):
        if i != j and mylist[i] + mylist[j] == target:
            ans.append(i)
            ans.append(j)
            flag = 1
    if flag == 1:
        break
print(ans)