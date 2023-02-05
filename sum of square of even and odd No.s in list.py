a=[]
even=0
odd=0
n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    x=int(input("Enter the elements: "))
    a.append(x)
for j in a:
    if j%2==0:
        even=even+j**2
    else:
        odd=odd+j**2
print('[',odd,',',even,']')
        
