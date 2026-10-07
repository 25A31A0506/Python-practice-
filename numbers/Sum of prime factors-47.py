#Find the sum of all distinct prime factors of a number.
num=int(input("Enter a number:"))
total=0
if num<=1:
    total=0
else:
    for i in range(2,num+1):
        count=0
        if num%i==0:
            for j in range(2,i):
                if i%j==0:
                    count+=1
            if count==0:
                total=total+i
print("sum is:",total)
