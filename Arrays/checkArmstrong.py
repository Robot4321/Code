# Python program to check if the number is an Armstrong number or not

# take input from the user
#num = int(input())

# initialize sum
#sum = 0

# find the sum of the cube of each digit
#temp = num
#while temp > 0:
   # digit = temp % 10
  #  sum += digit ** 3
 #   temp //= 10

# display the result
#if num == sum:
#    print("true")
#else:
 #   print("false")

def armstrong(n):
    number = str(n)

    n = len(number)
    output = 0
    for i in number:
        output = output+int(i)**n
    num = int(number)
    output = int(output)
    if output == num:
        print("true")
    else:
        print("false")


m = int(input())
armstrong(m)