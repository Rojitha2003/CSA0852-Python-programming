yr=float(input("Enter the year= "))
if(yr<=0):
    print("INVALID ENTRY")
else:
    if(yr%400==0):
            print("Leap year")
    elif(yr%100==0):
            print("Non leap year")
    elif(yr%4==0):
            print("Leap year")
    else:
            print("Non leap year")
            pre=yr-3
            print("Leap year ",pre)
