#Find the Sum of Digits Raised to Decreasing Powers
num=int(input())
temp=num
count=0
total=0
while num>0:
    rem=num%10
    count+=1
    num=num//10
while temp>0:
    remm=temp%10
    total=total+remm**(count)
    count-=1
    temp=temp//10
print("Total:",total)
