#Print all perfect squares from 1 to N.
num=int(input("Enter a number:"))
if num==0:
    print("0")
else:
    for i in range(1,(num//2)+1):
        square=i*i
        if square<=num:
            print(square)
