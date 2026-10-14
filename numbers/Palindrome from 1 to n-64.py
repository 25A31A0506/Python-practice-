#print all palindrome numbers from 1 to N.
num=int(input("Enter a number:"))
for i in range(num+1):
    temp=i
    n=temp
    reverse=0
    while n>0:
        rem=n%10
        reverse=reverse*10+rem
        n=n//10
    if temp==reverse:
        print(temp)
