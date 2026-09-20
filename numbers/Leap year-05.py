#Check whether a year is a leap year.
num=int(input())
if num%400==0:
    print("leap year")
elif num%100==0:
    print("not a leap year")
elif num%4==0:
    print("leap year")
else:
    print("not a leap year")
