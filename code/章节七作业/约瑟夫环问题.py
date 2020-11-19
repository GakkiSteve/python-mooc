n = int(input())
m = int(input())
mylist = []
ans = []
index = 0
for i in range(n):
    mylist.append(i)
while len(mylist) != 0:
    for i in range(m):
        index += 1
    index -= 1
    index = index % len(mylist)
    #print("index", index)
    #print("1mylist", mylist)

    tmp = mylist.pop(index)
    #print("2mylist", mylist)

    #print("tmp", tmp)
    ans.append(tmp)
    #print("ans", ans)
print(ans)