#print all numbers from 1 to N that are dividible by 4 or 6, but not divisible by 8.
num=int(input("Enter a number:"))
if num==0:
    print("no")
else:
    for i in range(1,num+1):
        if (i%4==0 or i%6==0) and i%8!=0:
            print(i)
