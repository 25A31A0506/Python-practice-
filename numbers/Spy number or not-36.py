#Check whether a number is a spy number.
num=int(input("Enter a number:"))
total=0
product=1
while num>0:
    rem=num%10
    total+=rem
    product*=rem
    num=num//10
if total==product:
    print("spy number")
else:
    print("Not a spy number")
