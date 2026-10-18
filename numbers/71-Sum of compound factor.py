#Find the sum of all compound factors of a number.
num=int(input("Enter a number:"))
total=0
if num==0:
    print("0")
else:
    for i in range(1,num+1):
        count=0
        if num%i==0:
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
            if count>2:
                total+=i
    print("sum is:",total)
