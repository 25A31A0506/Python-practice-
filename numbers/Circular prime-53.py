#Check whether a number is a circular prime.
#A circular prine is a number where every rotation of its digits is prime.
num=int(input("Enter a number:"))
temp=num
count=0
while num>0:
    count+=1
    num=num//10
original=temp
flag=True
for i in range(count):
    count1=0
    for j in range(1,original+1):
        if original%j==0:
            count1+=1
    if count1!=2:
        flag=False
        break
    first=original//(10**(count-1))
    rest=original%(10**(count-1))
    original=rest*10+first
if flag:
    print("Circular prime")
else:
    print("Not a circular prime")
