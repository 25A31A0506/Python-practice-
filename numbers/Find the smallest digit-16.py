#Find the smallest digit in a number.
num=int(input("Enter a number:"))
smallest=9
if num==0:
    smallest=0
else:
   while num>0:
       rem=num%10
       if rem<smallest:
           smallest=rem
       num=num//10
print(smallest)
