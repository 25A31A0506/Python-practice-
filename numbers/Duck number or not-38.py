#check whether a number is a duck number.
num=int(input())
temp=num
temp1=temp
count1=1
count2=0
while num>=10:
    count1=count1*10
    num=num//10
while temp>0:
    rem=temp%10
    if rem==0:
        count2=count2+1
    temp=temp//10
if count2>0 and temp1//count1!=0:
    print("Duck number")
else:
    print("Not a duck number")
