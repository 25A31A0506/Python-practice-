#Find the next prime number ofter a given number.
num=int(input("Enter a number:"))
n=num+1
while n>0:
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("Next prime number is:",n)
        break
    n+=1
