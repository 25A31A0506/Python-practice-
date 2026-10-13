#Find the difference between the largest and smallest digit of a number.
num=int(input("Enter a number:"))
largest=0
smallest=9
if num==0:
    print("Difference is:",0)
else:
    while num>0:
        rem=num%10
        if rem>largest:
            largest=rem
        if rem<smallest:
            smallest=rem
        num=num//10
    print("Difference is:",largest-smallest)
