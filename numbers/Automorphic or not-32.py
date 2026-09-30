#check whether a number is an Automorphic number.
num=int(input())
temp=num
sqare=num*num
count=1
while num>0:
    rem=num%10
    count=count*10
    num=num//10
remm=sqare%count
if temp==remm:
    print("Automorphic number")
else:
    print("not an automorphic number")
