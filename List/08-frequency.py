#Find the frequency of given element in a list.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
key=int(input("Enter a element:"))
count=0
for i in number:
    if i==key:
        count+=1
print("Frequency=",count)
