n = int(input("Enter the number of *'s needed to be printed :"))

i = 1
while i <= n:
    j = 1
    while j <=n:
        print("*",end="")
        j = j+1
    i = i + 1
    print("")

# For loop Solution
print("For Loop Solution")
for k in range(1, n+1):
    for l in range(1 , n+1):
        print("*", end="")
    print("")