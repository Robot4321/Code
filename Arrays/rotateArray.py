#O(n) Time and O(1) Space Complexity

def rotateArray1(arr,k):
    #array is divided into 3 parts and reversed 
    
    k = k % len(arr)
    l, r = 0 , len(arr) - 1  
    while l<r:
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
    print(arr)
    # reverse form 0 to k -  1
    l, r = 0 , k - 1 
    while l < r:
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
    print(arr)
    # reverse from k to n -1
    l, r = k, len(arr) - 1
    while l < r:
        arr[l],arr[r] = arr[r],arr[l]
        l += 1
        r -= 1
    print(arr)
    

# O(n) Time and O(n) Space
def rotateArray(arr,k):
    arr1 = [0] * len(arr)
    for i in range(len(arr)):
        
        #fromulae for array rotation is\
        x = (i+k)%len(arr)

        #print(x)
        arr1[x] = arr[i]
    
    print(*arr1 , sep=' ')
    print()
    print(*arr, sep=' ')

# (i+k)%len(arr)

arr = [1, 3, 6, 11, 12, 17, 22, 26, 30, 33, 38 ]
k =  7 
rotateArray1(arr,k)


# a = "abce" >= "abcdef"
# print(a)