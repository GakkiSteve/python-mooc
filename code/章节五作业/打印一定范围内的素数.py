import math
def isprime(n):
    tmp = int(math.sqrt(n))+1
    if tmp >= n:
        tmp = n -1
  
    for i in range(2, tmp):
        if n % i == 0:
            return False
    return True

ans = []
n = int(input())
for i in range(2, n):
    if isprime(i) == True:
        ans.append(i)
print(ans)