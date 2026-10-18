#Check whether number is a Empire number.
num=int(input("Enter a number:"))
temp=num
count1=0
count2=0
if num==0:
    print("Not am emirp number")
else:
    for i in range(1,num+1):
        if num%i==0:
            count1+=1
    if count1==2:
        reverse=0
        while num>0:
            rem=num%10
            reverse=reverse*10+rem
            num=num//10
        for j in range(1,reverse+1):
            if reverse%j==0:
                count2+=1
        if count2==2 and temp!=reverse:
            print("Emirp number")
        else:
            print("Not an emirp number")
    else:
        print("Not an emirp number")
