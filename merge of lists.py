a=[]
b=[]
c=[]
n=int(input("Enter the number of elements in first list:"))
for i in range(0,n):
    x=int(input("Enter elements:"))
    a.append(x)
m=int(input("Enter the number of elements in second list:"))
for j in range(0,m):
    y=int(input("Enter elements:"))
    b.append(y)
c=a+b
c.sort()
print("Third list=",c)
