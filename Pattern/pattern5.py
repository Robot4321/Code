n = int(input())
i=0
val=1
while( i < n):
    space=1
    while(space < n-i):

        print(" ", end = " ")
        space = space + 1
    j = 0
    while(j < val):

        print("*", end = " ")
        j = j + 1

    val = val+2
    print("")
    i = i + 1