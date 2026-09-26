#Check whether a number is a Strong number.
num=int(input())
temp=num
sum=0
while num>0:
    rem=num%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if sum==temp:
    print("strong number")
else:
    print("not a strong number")
