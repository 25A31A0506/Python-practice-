#Separate positive numbers, negative numbers and zero into three different lists.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
current=[number[0]]
longest=[number[0]]
for i in range(1,n):
    if number[i]==number[i-1]+1:
        current.append(number[i])
    else:
        if len(current)>len(longest):
            longest=current
        current=[number[i]]
if len(current)>len(longest):
    longest=current
print(longest)
