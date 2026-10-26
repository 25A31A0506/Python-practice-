#Merge two listes into one list.
n1=int(input("Size1 is:"))
list1=[]
for i in range(n1):
    list1.append(int(input()))
n2=int(input("Size2 is:"))
list2=[]
for i in range(n2):
    list2.append(int(input()))
merge=[]
for num in list1:
    merge.append(num)
for num in list2:
    merge.append(num)
print("merge list:")
print(merge)
