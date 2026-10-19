#Print all numbers from 1 to N that are divisible by 3 or 7 and not divisible by 5 and have an even last digit.
num=int(input("Enter a number:"))
if num==0:
    print("No numbers")
else:
    for i in range(1,num+1):
        if (i%3==0 or i%7==0) and i%5!=0:
            if i>0:
                rem=i%10
            if rem%2==0:
                print(i)
