#Find the sum of digits of a number.
num=int(input())
sum_result=0
while num>0:
    rem=num%10
    sum_result+=rem
    num=num//10
print(sum_result)
