a = int(input("Enter Value of 1st number: "))
b = int(input("Enter value of 2nd number: "))
c = int(input("Enter value of 2nd number: "))

if(a > b & a > c):
    print(a," is the largest")
elif( b> a & b > c):
    print(b," is the largest")
else:print(c," is the largest")