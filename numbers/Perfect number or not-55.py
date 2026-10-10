#check whether a numver is a perfect square
num=int(input("Enter a number:"))
if num<0:
    print("Not a perfect square")
else:
    for i in range(num+1):
        if i*i==num:
            print("Perfect square")
            break
    else:
        print("Not a perfect square")
