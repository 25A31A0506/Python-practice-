#Reversing the list without using reverse().
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
print("Reverse list")
for i in range(len(number)-1,-1,-1):
    print(number[i],end=" ")
