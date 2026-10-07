#Find the smallest prime factor of a number.
num=int(input("Enter a number:"))
if num<=0:
    print("no prime factor")
else:
    for i in range(2,num+1):
        if num%i==0:
            print("smallest prine factor:",i)
            break
