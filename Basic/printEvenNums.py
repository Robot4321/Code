n = int(input("Enter the digit till the even numbers need to be printed"))
x = list(range(0 , n))
i = 0;
for i in x:
    if(x[i]%2 == 0 ):
        print(x[i])
        i = i+1
