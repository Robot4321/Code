from re import M


def binary_searchN(arr, low, high, x):
    #print(high,low,x)
    #mid = 0
    if high == 0:
        return -1
    elif high >= low:

        while low <= high:
            mid = (high + low)//2
           # print(arr[mid])

            if arr[mid] == x:
                return mid
            elif x > arr[mid]:
                low = mid + 1
            elif x < arr[mid]:
                high = mid - 1
            else:
                return -1

    else:
        return -1


def binary_searchR(arr, low, high, x):
    #mid = 0
    print(high,low,x)

    if high >= low:

        mid = (low + high)//2
        print(low,mid,high,x)

        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            binary_searchR(arr, mid + 1, high, x)
        else:
            binary_searchR(arr, low, mid - 1, x)

    else:
        return -1


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

x1 = 19
low1 = 0
high1 = len(arr1)

print(binary_searchN(arr1, 0, len(arr1) - 1, x1))

print(binary_searchR(arr1, 0, len(arr1) - 1 , x1))
