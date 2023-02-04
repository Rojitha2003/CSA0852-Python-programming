rows=int(input("Enter number of rows :"))
number=1
for i in range(1,rows+1):
    for j in range(1,rows-i+1):
        print(" ",end="")
    for k in range(0,i):
        if k==0 or i==0:
            number=1
        else:
            number=number*(i-k)//k
        print(number,end=" ")
    print()
