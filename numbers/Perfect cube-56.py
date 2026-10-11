#check whether a numver is a perfect cube.
num=int(input("Enter a number:"))
if num<0:
    print("Not a perfect cube")
else:
    for i in range(num+1):
         if i*i*i==num:
             print("Perfect cube")
             break
    else:
        print("Not a perfect cube")
