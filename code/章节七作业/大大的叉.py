n = int(input())
maxx = (n-1)*2 + 1
firstpart = secondpart = n - 1
for i in range(firstpart):
    print(i*"+"+"X"+(maxx-2*i-2)*"+"+"X"+i*"+")
print((n-1)*"+"+"X"+(n-1)*"+")
for i in range(secondpart-1,-1,-1):
    print(i*"+"+"X"+(maxx-2*i-2)*"+"+"X"+i*"+")