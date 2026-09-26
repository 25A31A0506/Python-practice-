# check whether number is a perfect number.
num=int(input())
temp=num
sum_result=0
for i in range(1,num):
    if num%i==0:
        sum_result=sum_result+i
if sum_result==num:
    print("perfect number")
else:
    print("not a perfect number")
