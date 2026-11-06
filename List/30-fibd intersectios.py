#Find the intersection of two lists(without duplicates).
n=int(input("Size is:"))
list1=[]
print("Enter list2:")
for i in range(n):
    list1.append(int(input()))
list2=[]
print("Enter list1:")
for i in range(n):
    list2.append(int(input()))
intersection=[]
for num1 in list1:
    for num2 in list2:
        if num1==num2 and num2 not in intersection:
            intersection.append(num2)
print(intersection)
