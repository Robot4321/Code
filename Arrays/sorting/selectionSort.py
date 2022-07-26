def selectionSort(arr):
    for i in range(len(arr)):
        #set min as the ith iteration
        min = i
        for  j in range(i+1, len(arr)):
            if arr[j]< arr[i]:
                #assign new min as j
                min = j
        # Swap Values
        arr[i],arr[min] = arr[min], arr[i]
    
    print(*arr, sep=" ")


arr = [1,2,34,66,7,33,2,5,6,9,0,66,3,1,3]

selectionSort(arr)   