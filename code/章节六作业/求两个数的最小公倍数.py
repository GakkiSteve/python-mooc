def lcm(num1, num2):
    maxx = num2
    while 1:
        if maxx % num1 == 0 and maxx % num2 == 0:
            break
        else:
            maxx += 1
    return maxx

num1=int(input(""))
num2=int(input(""))
print(lcm(num1,num2))