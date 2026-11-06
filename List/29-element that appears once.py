#Find the element that appears only once when every other element appears exactly twice.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
for i in range(n):
    count=0
    for j in range(n):
        if number[i]==number[j]:
            count+=1
    if count==1:
        print("Result is:")
        print(number[i])
