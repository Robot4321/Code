def largestColumn(arr):
    
    maxColSum = -1
    colindex = 0

    n,m = len(arr), len(arr[0])

    for j in range(m):
        colSum = 0
        for i in range(n):
            colSum += arr[i][j]
            print(arr[i][j])
        
        if colSum > maxColSum:
            maxColSum = colSum
            colindex = j
    return colindex, maxColSum

def largestRow(arr):
    
    maxRowSum = -1
    rowindex = 0
    
    n,m = len(arr), len(arr[0])    
    for i in range(n):
        rowSum=0
        for j in range(m):
            rowSum += arr[i][j]
        if rowSum > maxRowSum:
            maxRowSum = rowSum
            rowindex = i
    return rowindex, maxRowSum


def takeinput():
    
    str1 = input().split()
    n,m = int(str1[0]), int(str1[1])
    arr1 = input().split()
    if len(arr1) == n*m:
        arr = [[int(arr1[(m*i)+j]) for j in range(m)] for i in range(n)]
        print()
        for i in arr:
            output = ' '.join([str(ele) for ele in i])
            print(output)
        print()
        cI, rSum = largestColumn(arr)
        rI, cSum = largestRow(arr)
        print(cSum,rSum)
        if rSum > rSum:
            print("RowSum ", rSum, rI)
        else:
            print("ColSum ", cSum, cI)
    
    else:
        print("Wrong Input")

takeinput()

