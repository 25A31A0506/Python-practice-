#Rotate a list to the right by one position
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
last=number[n-1]
for i in range(n-1,0,-1):
    number[i]=number[i-1]
number[0]=last
print("After rotate:")
print(number)
