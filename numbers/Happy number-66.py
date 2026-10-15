#Check whether a number is a Happy Number.
num=int(input("Enter a number:"))
while num!=1 and num!=4:
    total=0
    while num>0:
        rem=num%10
        total+=rem*rem
        num=num//10
    num=total
if num==1:
    print("Happy number")
else:
    print("Not a happy number")
