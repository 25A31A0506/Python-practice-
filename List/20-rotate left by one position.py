#Rotate a list to the left by one position.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
first=number[0]
for i in range(n-1):
    number[i]=number[i+1]
number[n-1]=first
print("After rotate:")
print(number)
