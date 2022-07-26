# Largest of n numbers in a list
# create list

len = int(input("Enter the number of elements to create an array of "))
list = []
for i in range(len):
    n = int(input("Enter array element "))
    list.append(n)

max = list[0]

for k in list:
    if (k > max):
        max = k
    break
print("Max = ", max)