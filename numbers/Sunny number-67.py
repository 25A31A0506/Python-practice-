#Check whether a number is a sunny number.
num=int(input("Enter a number:"))
if num==0:
    print("Sunny number")
elif num<0:
        print("Not a sunny number")
else:
    square=num+1
    for i in range(1,square):
        if i*i==square:
            print("Sunny number")
            break
    else:
        print("Not a sunny number")
