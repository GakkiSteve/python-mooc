n = int(input())
mylist = str(n)
length = len(mylist)
flag = "yes"
for i in range(0,length//2+1):
    if mylist[i] != mylist[-(i+1)]:
        flag = "no"
        break
print(flag)