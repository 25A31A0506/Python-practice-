#Find the unique elements from two lists.
n1=int(input("Size1 is:"))
list1=[]
for i in range(n1):
    list1.append(int(input()))
n2=int(input("Size2 is:"))
list2=[]
for i in range(n2):
    list2.append(int(input()))
unique=[]
for num in list1:
    if num not in list2 and num not in unique:
        unique.append(num)
for num in list2:
    if num not in list1 and num not in unique:
        unique.append(num)
print("common elements is:")
print(unique)
