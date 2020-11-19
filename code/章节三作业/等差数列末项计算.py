a = int(input())
b = int(input())
c = int(input())-1
d = b - a
last = a
for i in range(c):
    last += d
print(last)