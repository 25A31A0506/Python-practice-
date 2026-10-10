#Print all numbers from 1 to N that are dividible by both 3 and 5 but not divisible by 2.
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if i%3==0 and i%5==0 and i%2!=0:
        print(i)
