#Remove the duplicate elements in a list.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
elements=[]
for num in number:
    if num not in elements:
        elements.append(num)
print("List after removal duplicates:")
for num in elements:
    print(num)
