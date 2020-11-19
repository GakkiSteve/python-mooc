n = int(input())
maxx = 1 + 2*(n-1)
starnum = 1
for i in range(n):
    print(((maxx-starnum)//2)*" "+(starnum*"+"))
    starnum += 2