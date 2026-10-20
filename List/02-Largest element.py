#Find the largest element in a list.
n=int(input("Size is:"))
number=[]
for i in range(n):
    x=int(input())
    number.append(x)
    largest=number[0]
for i in range(n):
    if number[i]>largest:
        largest=number[i]
print(largest)
