#Check whether a given number is present in the list.
n=int(input("Size is:"))
number=[]
key=int(input("Enter number:"))
for i in range(n):
    number.append(int(input()))
if key in number:
    print("Element found")
else:
    print("Element not found")
