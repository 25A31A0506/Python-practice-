#Find the second largest element in a list.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
if n<2:
    print("Second largest element is not existed")
else:
    if number[0]>number[1]:
        largest=number[0]
        second_largest=number[1]
    else:
        largest=number[1]
        second_largest=[0]
    for i in range(2,n):
        if number[i]>largest:
            second_largest=largest
            largest=number[i]
        elif number[i]>second_largest and number[i]<largest:
            second_largest=number[i]
    print(second_largest)
