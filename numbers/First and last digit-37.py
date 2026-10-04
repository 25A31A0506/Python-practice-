#Find the first and last digit of a number.
num=int(input("Enter a number:"))
temp=num
count=1
while num>=10:
    rem=num%10
    count=count*10
    num=num//10
first_digit=temp//count
last_digit=temp%10
print("first digit:",first_digit)
print("last digit:",last_digit)
