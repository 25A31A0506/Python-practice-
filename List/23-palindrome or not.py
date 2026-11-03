#check whether a list is a palindrome.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
rotate=[]
for i in range(n-1,-1,-1):
    rotate.append(number[i])
if number==rotate:
    print("Palindrome")
else:
    print("Not a palindrome")
