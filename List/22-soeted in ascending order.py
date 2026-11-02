#Check whether a list is sorted in ascending order.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
for i in range(n-1):
    if number[i]>number[i+1]:
        print("List is not sorted")
        break
else:
    print("List is sorted")
