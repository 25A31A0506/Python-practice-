#Check whether two numbers are Amicable numbers.
num1=int(input())
num2=int(input())
sum1=0
sum2=0
for i in range(1,num1):
    if num1%i==0:
        sum1=sum1+i
for j in range(1,num2):
    if num2%j==0:
        sum2=sum2+j
if sum1==num2 and sum2==num1:
    print("Amicable number")
else:
    print("not an amicable number")
