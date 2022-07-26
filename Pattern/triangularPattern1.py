n = int(input("Enter the number of rows to print the triangular pattern of :"))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print("")

print(" ")

for k in range(1, n+1):
    m = k
    for l in range(1, k+1):
        print(m, end="")
        m = m + 1
    print("")
