M = int(input("Enter the starting number(M): "))
N = int(input("Enter the ending number(N): "))
if N<M:
    print("Invalid input")
elif M==N:
    print("Starting and ending numbers are same")
else:
    K = int(input("Enter the numbers to be skipped in range(K): "))
    if(K<0):
        print("K value is negative-INVALID INPUT")
    for i in range(M, N+1, K+1):
        print(i)
