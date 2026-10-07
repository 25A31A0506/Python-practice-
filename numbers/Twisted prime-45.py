#Check whether a number us a twisted prime.
#A number is prine, and its reverse is also prime. 
num=int(input("Enter a number:"))
reverse=0
count1=0
count2=0
for i in range(2,num):
    if num%i==0:
        count1+=1
if count1==0:
    while num>0:
        rem=num%10
        reverse=reverse*10+rem
        num=num//10
    for j in range(2,reverse):
        if reverse%j==0:
            count2+=1
    if count2==0:
        print("Twisting prime")
    else:
        print("Not a twisting prime")
else:
    print("not a prime")
