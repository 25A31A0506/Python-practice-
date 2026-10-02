#Check whether a number is a Harshad (Niven) Number.
num=int(input())
temp=num
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if temp%sum==0:
    print("Harshad number")
else:
    print("not a harshad number")
