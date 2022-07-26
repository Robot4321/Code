n = int(input("Enter the number: "))
x = list(range(2, n))
flag = False
if( n > 1):
    for i in x:
            if(n%x[i] == 0):
                flag = True
                print(x[i])
            break
if (flag == True):
    print("Not a prime number")
else:
    print("It is a prime number")