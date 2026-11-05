#Print all pairs whose product is equal to a given number.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
target=int(input("Enter target:"))
print("Pairs are:")
for i in range(n):
    for j in range(i+1,n):
        if number[i]*number[j]==target:
            print(number[i],number[j])
