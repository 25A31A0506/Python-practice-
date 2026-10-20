#Find the smallest element in a list.
n=int(input("Size is:"))
number=[]
for i in range(n):
    x=int(input())
    number.append(x)
    smallest=number[0]
for i in range(n):
    if number[i]<smallest:
        smallest=number[i]
print(smallest)
