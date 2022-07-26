def printArray(arr):
    n = len(arr)
    m = len(arr[0])
    k = n
    for i in arr:
        while k <= n:
            print(*i, sep= ' ')
        k -=1

arr = [[1,2,3],[4,5,6],[7,8,9]]
printArray(arr)






# #include <iostream>
# using namespace std;

# void print2DArray(int **input, int row, int col) {
	
    
#     int k = row;
    
#     for(int i = 0; i< row ;i++){
#         for (int j =k-1; j >=0 ; j--){
#             for (int l = 0 ;l < col; l++){
#                 cout << input[i][l] << " ";
#             }
#             cout << endl;
#         }
#         k --;
    
#     }

# }


