
# O(n^2) Time Complexity O(1) Space Complexity
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(*arr, sep=",")


def optimizeBUbbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(*arr,sep=",")
    #Passes (n -2)(n - 1)

arr = [7,5,8,9,6,3,2,5,4,7,8,5,8,9,5,4,1,2,3,96,7]
bubbleSort(arr)
optimizeBUbbleSort(arr)