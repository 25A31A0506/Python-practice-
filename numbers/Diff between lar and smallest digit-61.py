#Find the difference between the largest and smallest digit of a number.
num=int(input("Enter a number:"))
temp=num
largest=0
if num==0:
    print("Difference is:",0)
else:
    while num>0:
        rem=num%10
        if rem>largest:
            largest=rem
        num=num//10
    smallest=9
    while temp>0:
        remm=temp%10
        if remm<smallest:
            smallest=remm
        temp=temp//10
    print("Difference is:",largest-smallest)
