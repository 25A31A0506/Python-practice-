#Find the largest difference between any two elements in a list.
n=int(input("Size is:"))
number=[]
largest=float('-inf')
smallest=float('inf')
for i in range(n):
    number.append(int(input()))
    if number[i]>largest:
        largest=number[i]
    if number[i]<smallest:
        smallest=number[i]
Difference=largest-smallest
print("Difference is:", Difference)
