def revParArray(arr, m):

    n = len(arr)
    
    #new Array = onld array till m + old array from n to m => arr[n:m:-1]
    
    arr1 = arr[0:m+1:1] + arr[n:m:-1]
    print(*arr1,sep=" ")    


arr = [1,2,5,8,7,4,5,6,9,5,88]
m = 4
revParArray(arr,m)
