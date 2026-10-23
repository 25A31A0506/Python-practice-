#Print all prime numbers present in the list
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
for i in number:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
         print(i)
