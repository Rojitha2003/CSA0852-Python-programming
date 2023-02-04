count_lower=0
count_upper=0
count_number=0
print("Enter * to Exit:")
for i in range(10):
    x=input("Enter any character:")
    if (x=='*'):
        break
    if(x.islower()):
        count_lower+=1
    elif(x.isupper()):
        count_upper+=1
    elif(x.isnumeric()):
        count_number+=1
print("The number of lowercase characters is:",count_lower)
print("The number of uppercase charcaters is:",count_upper)
print("count of numbers is:",count_number)
