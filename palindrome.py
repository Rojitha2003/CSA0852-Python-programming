n=int(input("Enter x:"))
temp=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
print(temp,"is palindrome")
if(temp==r):
    print("True")
else:
    print("False")
