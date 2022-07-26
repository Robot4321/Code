# Write your code here
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if(x2 > x1) & (y2 > y1):
    area = (x2 - x1) * (y2 - y1)
    print(area)
else:
    print("Wrong inputs!")

x = 5
if x < 6:
    print("Hello")
if x == 5:
    print("Hi")
else:
    print("Hey")