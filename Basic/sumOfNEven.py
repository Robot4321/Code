n = int(input())
sum = 0
#for loop
for i in range(1, n+1):
    if((i % 2) == 0):
        sum = sum + i
print("using for loop ",sum)

k = 0
sum1 = 0
while(k <= n):
    if((k % 2) == 0):
        sum1 = sum1 + k
    k = k + 1
print("using while loop", sum1)