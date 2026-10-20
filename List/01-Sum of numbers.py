#Find the sum of all elements in a list.
n=int(input("size is:"))
number=[]
total=0
for i in range(n):
    number.append(int(input()))
    total+=number[i]
print(total)
