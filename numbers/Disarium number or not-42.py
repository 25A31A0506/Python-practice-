#Check whether a number is a Disarium number.
num=int(input())
temp1=num
temp2=temp1
count=0
total=0
while num>0:
    rem=num%10
    count+=1
    num=num//10
while temp1>0:
    remm=temp1%10
    total=total+remm**(count)
    count-=1
    temp1=temp1//10
if temp2==total:
    print("Disarium number")
else:
    print("Not a disarium number")
