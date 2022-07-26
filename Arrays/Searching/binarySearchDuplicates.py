from distutils.command.build_scripts import first_line_re


def binary_search(arr,x,dupes):
    high = len(arr) - 1
    low = 0
    res = -1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == x:
            res = mid
            if dupes == True:
                high = mid - 1
            else:
                low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1 
    return res



a = [1,2,3,3,4,5,6,6,9,8,7]
firstIndex = binary_search(a,6,True)

if(firstIndex == None):
    print ("Count = 0")
else:
    lastIndex = binary_search(a,3,False)
    print("Count = ", lastIndex - firstIndex + 1)