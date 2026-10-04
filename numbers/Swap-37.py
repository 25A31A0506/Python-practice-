#swap the first and last digit of a number.
num=int(input())
temp=num
count=1
while num>=10:
    count=count*10
    num=num//10
first=temp//count
last=temp%10
middle=(temp%count)//10
swapped=last*count+middle*10+first
print(swapped)
