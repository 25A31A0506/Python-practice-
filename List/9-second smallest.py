#Find the second smallest element in a list
n=int(input("Size is:"))
number=[]
smallest=float('inf')
second_smallest=float('inf')
for i in range(n):
    number.append(int(input()))
for num in number:
    if num<smallest:
        second_smallest=smallest
        smallest=num
    elif num<second_smallest and num!=smallest:
        second_smallest=num
if second_smallest==float("inf"):
    print("No second smallest element")
else:
    print("second smallest is:",second_smallest)
