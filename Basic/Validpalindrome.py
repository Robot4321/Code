from operator import le
from turtle import right


def isPalindromeStrMethod(a):
    a1 = str(a)
    if a1[::-1] == a1:
        print("True")
        return True
    else:
        print("False")
        return False

def isStringPalindrome(string):
    left = 0
    right = len(string) - 1
    while left<right:
        if string[left] != string[right]:
            print("False!")
            return False
        else:
            right -= 1
            left += 1
    print("True")

def isPalindrome(a):
    #if the number is zero and the number is a multiple of 10 then invalid palindrome
    rev = 0
    if a <= 0 or a % 10 == 0:
        print("False")
    while(a > rev):
        rev = rev * 10 + a % 10 
        a  = a //10
    print(a,rev)
    if a == rev or a == rev//10 :
        print ("True")
    else:
        print("False")

n = int(input("Enter Valid Number:"))
#isPalindromeStrMethod(n)
isPalindrome(n)
isStringPalindrome("whattah")

