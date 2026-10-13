#Check whether a number is a buzz number.
num=int(input("Enter a number:"))
if num==0:
    print("Not a buzz number")
else:
    if num>0:
        rem=num%10
        if rem==7 or num%7==0:
            print("Buzz number")
        else:
            print("Not a buzz number")
