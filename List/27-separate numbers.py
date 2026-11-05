#Separate positive numbers, negative numbers and zero into three different lists.
n=int(input("Size is:"))
number=[]
for i in range(n):
    number.append(int(input()))
zero=[]
negative=[]
positive=[]
for num in number:
    if num==0:
        zero.append(num)
    elif num<0:
        negative.append(num)
    else:
        positive.append(num)
print(zero)
print(negative)
print(positive)
