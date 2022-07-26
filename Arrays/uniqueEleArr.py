
#O(n^2)
def findUnique(arr , n):
    for i in range(n):
        count = 0

        for j in range(n):
            if i != j and arr[i] == arr[j]:
                count = count + 1

        if count == 0:
            print (arr[i])

def findUniqueEle2(arr):
    isExistEle = {}
    for i in range(len(arr)):
        isExistEle[arr[i]] = i
    
    print(list(isExistEle.keys()))
arr = [5,6,9,7,7,8,7,7,5,6]

n = len(arr)

findUnique(arr,n)
#findUniqueEle2(arr)