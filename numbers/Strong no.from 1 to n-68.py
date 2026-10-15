#Print all strong numbers from 1 to N.
num=int(input("Enter a number:"))
if num==0:
    print("0")
else:
    if num>0:
        for i in range(1,num+1):
            temp=i
            total=0
            while temp>0:
                rem=temp%10
                fact=1
                for j in range(1,rem+1):
                    fact=fact*j
                total+=fact
                temp=temp//10
            if total==i:
                print(i)
