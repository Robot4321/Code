#swapping
#O(n) time and O(1) Space
def reverse(arr):
    n = len(arr)

    for i in range(n//2):
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]

#-ve indexking and swapping
def reverse2(arr):
    n = len(arr)

    for i in range(n//2):
        arr[i],arr[-i-1] = arr[-i-1],arr[i]
   
#Indexing
def reverse3(arr):

    print(arr[len(arr):0:-1])
    print(arr[::-1])


arr = [1,2,3,4,5,6,7,8,9,10]
arr1 = [11,12,13,14,15,16,17,18,19,20]
arr2 = [21,22,23,24,25,26,27,28,29,30]
reverse(arr)
reverse2(arr1)
print (*arr, sep=' ')
print (*arr1, sep= ' ')
reverse3(arr2)