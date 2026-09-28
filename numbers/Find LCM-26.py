#Find the LCM of two numbers.
num1=int(input())
num2=int(input())
if num1<num2:
    for i in range(1,num1+1):
        if num1%i==0 and num2%i==0:
            GCD=i
else:
    for i in range(1,num2+1):
        if num1%i==0 and num2%i==0:
            GCD=i
LCM=(num1*num2)//GCD
print(LCM)
