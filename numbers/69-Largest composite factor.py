#Find the largest composite factor of a number.
num=int(input("Enter a number:"))
if num==0:
    print("No factor")
else:
    LCF=-1
    for i in range(1,num+1):
        if num%i==0:
            count=0
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
        if count>2:
            LCF=i
    if LCF==-1:
        print("No composite factor")
    else:
        print(LCF)
