#Reverse the digits and check whether the reversed number is greater than the original number.
num=int(input())
temp=num
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if reverse>temp:
    print("greater")
else:
    print("not greater")
