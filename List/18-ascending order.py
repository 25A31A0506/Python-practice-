#Sort a list in ascending order without using sort().
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
for i in range(n-1):
    for j in range(n-1-i):
        if number[j]>number[j+1]:
            temp=number[j]
            number[j]=number[j+1]
            number[j+1]=temp
print("After sorting:")
print(number)
