#Check whether a number is a Palindrome Prime.
#A number is a palindrome and a prime number
num=int(input("Enter a number:"))
temp=num
count=0
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if temp!=reverse:
    print("not a palindrome")
else:
    for i in range(2,temp):
       if  temp%i==0:
           count+=1
    if count==0:
        print("palindrome prime")
    else:
        print("Not a palindrome prime")
