def pairSum(arr,s):
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == s:
                print(arr[i],arr[j], sep=' ')






arr = [1,5,2,6,3,9,9,8]

pairSum(arr,18)