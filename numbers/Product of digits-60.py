#Find the product of all digits of a number
num=int(input("Enter a number:"))
product=1
if num==0:
    product=0
else:
    while num>0:
        rem=num%10
        product*=rem
        num=num//10
print(product)
