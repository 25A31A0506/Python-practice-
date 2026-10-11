#Find the sum of all factors of a number.
num=int(input("Enter a number:"))
total=0
for i in range(1,num+1):
    if num%i==0:
        total+=i
print("sum is:",total)
