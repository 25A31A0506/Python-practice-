#Count the number of digits in a number.
num=int(input())
if num==0:
    count=1
else:
    count=0
    while num>0:
        count+=1
        num=num//10
print(count)
