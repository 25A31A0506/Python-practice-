#Check whether a number is a palindrome.
num=int(input())
temp=num
reverse=0
while num>0:
rem=num%10
reverse=reverse*10+rem
num=num//10
if reverse==temp:
print("palindrome")
else:
print("not a palindrome")
