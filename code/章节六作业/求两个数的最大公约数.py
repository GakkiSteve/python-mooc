def hcf(num1, num2):
    # Euclidean algorithm
    b = max(num1, num2)
    a = min(num1, num2)
    quotient = b//a
    remainder = b - quotient*a
    #print("quotient:",quotient,"remainder:",remainder)
    while remainder != 0:
        b = a
        a = remainder
        quotient = b//a
        remainder = b - quotient*a
        #print("quotient:",quotient,"remainder:",remainder)

    return a

num1=int(input(""))
num2=int(input(""))
print(hcf(num1,num2))