a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
if((a+b>c)|(a+c > b) | (c+b > a) ):
    print("It is a Valid Triangle!")
else:print("Not a valid triangle!")