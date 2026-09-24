#Print even numbers from 1 to N
N=int(input("Enter a number:"))
for i in range(1,N+1):
    if i%2==0:
        print(i)
