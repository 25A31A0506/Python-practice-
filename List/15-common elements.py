#Find the common elements present in two lists.
n1=int(input("Size1 is:"))
list1=[]
for i in range(n1):
    list1.append(int(input()))
n2=int(input("Size2 is:"))
list2=[]
for i in range(n2):
    list2.append(int(input()))
element=[]
for i in list1:
    for j in list2:
        if i==j:
            element.append(i)
print("common elements is:")
print(element)
