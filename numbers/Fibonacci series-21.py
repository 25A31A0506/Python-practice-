#Print the Fibonacci series up to N terms.
num=int(input())
fir=0
sec=1
while num>0:
    print(fir)
    third=fir+sec
    fir=sec
    sec=third
    num=num-1
