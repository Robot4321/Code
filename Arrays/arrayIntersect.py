from asyncio.windows_events import NULL
from collections import Counter
from pyparsing import null_debug_action
from requests import NullHandler


# O(n^2) Time Complexity
def intersectArr1(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                print(arr1[i], end=" ")
                arr2[j] = NULL
                break

# sorted VErsion
# O(n) Complexity Time

def intersectArr2(arr1, arr2):

    arr3 = []
    arr1, arr2 = sorted(arr1), sorted(arr2)

    i, j = 0, 0

    n, m = len(arr1), len(arr2)

    while i < n and j < m:

        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            arr3.append(arr1[i])
            i += 1
            j += 1

    print(*arr3, sep=' ')


# count Object
# O(n) Space

def intersectArr3(arr1, arr2):

    c = Counter(arr1)
    arr3 = []
    for i in arr2:
        if c[i] > 0:
            arr3.append(i)
            c[i] -= 1

    print(*arr3, sep=' ')


arr1 = [1, 1, 2, 3, 9, 5, 6]
arr2 = [1, 2, 6, 5,6,2]


#intersectArr1(arr1, arr2)
#intersectArr2(arr1, arr2)
intersectArr3(arr1, arr2)
