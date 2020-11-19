x = int(input())
y = int(input())
n = int(input())

def select(x, y, n):
    r = set()
    for i in range(n):
        for j in range(n):
            tmp = x**i + y**j
            if tmp<=n:
                r.add(tmp)
    return sorted(r)
print(select(x, y, n))