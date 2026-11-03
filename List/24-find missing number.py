#Find the missing number in a list containing numbers from 1 to n.
n=int(input("Size is:"))
number=[]
for i in range(n-1):
    number.append(int(input()))
expected_sum=n*(n+1)//2
actual_sum=0
for num in number:
    actual_sum+=num
missing=expected_sum-actual_sum
print("missing number:",missing)
