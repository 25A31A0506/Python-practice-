#Move all even eliments to the biginng of the list and odd numbers to the end.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
element=[]
for num in number:
    if num%2==0:
        element.append(num)
for num in number:
    if num%2!=0:
        element.append(num)
print("After reset:")
print(element)
