# line Separated
"""
n = int(input("Enter the number of elements of the list:"))

# create an empty list
li = []
for i in range(n):
    curr = int(input("Enter the list element: "))
    li.append(curr)


for i in range(len(li)):
    print(li[i])
"""
# Space Separate Input

# take input as string

n = input("Enter the List Elements: ")

# use String Split on it

str_split = n.split()
li = []
for i in range(len(str_split)):
    li.append(int(str_split[i]))

print(li)

lj = [int(x) for x in input().split()]
