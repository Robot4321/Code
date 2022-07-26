# Function to print pattern
def print_arrow(n):

    # for printing upper part
    # of the arrow
    for i in range(1,n):

        # To give space before printing
        # stars in upper part of arrow
        for j in range(0,i):
            print(" ",end="")


        # To print stars in upper
        # part of the arrow
        for k in range(0,i):
            print("*",end=" ")

        print()


    # for printing lower part
    # of the arrow
    for i in range(0,n):

        # To give space before printing
        # stars in lower part of arrow
        for j in range (0,n-i):
            print(" ",end="")


        # To print stars in lower
        # part of the arrow
        for k in range (0,n-i):
            print("*",end=" ")

        print()

#driver code

n = int(input())

# function calling
print_arrow(n)