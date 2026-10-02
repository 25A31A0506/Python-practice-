#Check whether a number us a Neon number.
num=int(input())
square=num*num
total=0
while square>0:
    rem=square%10
    total=total+rem
    square=square//10
if num==total:
    print("Neon number")
else:
    print("not a neon number")
