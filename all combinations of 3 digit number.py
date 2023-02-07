num=int(input("Enter 3 digit number:"))
if(num>99 and num<1000):
    l=[]
    a=int(input("Enter first digit of given number:"))
    b=int(input("Enter second digit of given number:"))
    c=int(input("Enter thrid figit of given number:"))
    if(a==b and b==c and b==a):
        print("Only one combination is possible:",a,b,c)
    else:
        print("Combinations:")
        l.append(a)
        l.append(b)
        l.append(c)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if(i!=j and j!=k and k!=i):
                        print(l[i],l[j],l[k])
else:
    print("Invalid")
    if(num<0):
        print("Please enter positive 3 digit number")
    else:
        print("Please enter 3 digit number")
