#print all armstrong number from 1 to N.
num=int(input("Enter a number:"))
for i in range(num+1):
    temp=i
    count=0
    while temp>0:
        count+=1
        temp=temp//10
    temp=i
    total=0
    while temp>0:
        rem=temp%10
        total=total+rem**count
        temp=temp//10
    if total==i:
        print("Armstrong number is:",i)
