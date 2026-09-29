#find the second largest digit in a number.
num=int(input())
largest=-1
second_largest=-1
while num>0:
    rem=num%10
    if rem>largest:
        second_largest=largest 
        largest=rem
    if rem>second_largest and rem<largest:
        second_largest=rem
    num=num//10
print(second_largest)
