#Convert a decimal number to binary without using bin().
num=int(input())
binary=""
if num==0:
    print(0)
else:
    while num>0:
        rem=num%2
        binary=str(rem)+binary
        num=num//2
print(binary)
