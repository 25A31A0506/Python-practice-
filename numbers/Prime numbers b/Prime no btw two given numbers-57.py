#print all prime numbers between two give numbers.
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
if num1==num2:
    print("No prime numbers")
else:
    for i in range(num1+1,num2):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            print(i)
