num = int(input())
for i in range(100,num+1):
    mylist = list(str(i))
    ans = 0
    n = len(mylist)
    for j in mylist:
        ans += int(j)**n
    if ans == i:
        print(i)