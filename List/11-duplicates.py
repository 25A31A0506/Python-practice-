#Print all duplicate elements in a list.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
duplicate=[]
for i in range(n):
    for j in range(i+1,n):
        if number[i]==number[j] and number[i] not in duplicate:
            duplicate.append(number[i])
if len(duplicate)==0:
    print("No duplicate elements")
else:
    print("Duplicate elements is:")
    for num in duplicate:
        print(num)
