#Check whether a number is an Armstrong number.
num=int(input())
num1=num
temp=num1
count=0
while num>0:
remm=num%10
count=count+1
num=num//10
result=0
while num1>0:
rem=num1%10
result=result+rem**count
num1=num1//10
if result==temp:
print("Armstrong number")
else:
print("not a armstrong number")
