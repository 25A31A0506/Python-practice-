#Find the largest prime factor of a number.
num=int(input("Enter a number:"))
largest=1
for i in range(2,num+1):
    if num%i==0:
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            largest=i
print("L.P.F",largest)
