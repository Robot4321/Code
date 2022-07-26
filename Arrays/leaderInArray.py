# #include <bits/stdc++.h>
# void Leaders(int* arr,int len)
# {
#  int j=len-1;
#     vector <int> v;
#     for (int i=len-1;i>=0;i--){
#         if(i==len-1){
#             v.push_back(arr[i]);
#             continue;
#         }
#         if(arr[i]>=arr[j]){
#             v.push_back(arr[i]);
#             j=i;
#         }
#     }
#     for (int i=v.size()-1;i>=0;i--){
#         cout<<v[i]<<" ";
#     }
# }
