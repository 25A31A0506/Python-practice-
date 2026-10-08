#Check whether two numbers are co-primes.
#Two numbers are co-primes if their GCD is 1
num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
if num1<num2:
    for i in range(1,num1+1):
        if num1%i==0 and num2%i==0:
            GCD=i
else:
    for j in range(1,num2+1):
        if num1%j==0 and num2%j==0:
            GCD=j
if GCD==1:
    print("co-primes")
else:
    print("not a co-prime")
