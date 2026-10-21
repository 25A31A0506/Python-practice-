#Count how many even and odd digits are present in a list.
n=int(input("Enter a number:"))
number=[]
count1=0
count2=0
for i in range(n):
    number.append(int(input()))
    if number[i]%2==0:
        count1+=1
    else:
        count2+=1
print("Even",count1)
print("odd",count2)
