#Find the frequency of each digit in a number.
num=int(input())
temp=num
for i in range(10):
    count=0
    temp=num
    if temp==0 and i==0:
        count=1
    else:
        while temp>0:
            rem=temp%10
            if rem==i:
                count+=1
            temp=temp//10
    if count>0:
        print(i,"-->",count,"times")
