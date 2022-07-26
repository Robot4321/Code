def minLength(str1):
    
    hashMap1 = {}
    hashMap2 = {}

    for i in str1:
        if i in hashMap1:
            continue
        else:
            hashMap1[i] = len(i)

    for i in range(len(str1)):
        if str1[i] in hashMap2:
            continue
        else:
            hashMap2[str1[i]] = i
    
    #min(hashMap1, key = hashMap1.get)
    print(hashMap2)






str1  =  "this is test string"
str1 = str1.split()

print(sorted(str1))
minLength(str1)


# */
# #include<cstring>
# void minLengthWord(char input[], char output[]){
#     int len = strlen(input);
#     int si = 0, ei = 0;
#     int min_length = len, min_start_index = 0;
#     while (ei <= len)
#     {
#         if (ei < len && input[ei] != ' ')
#             ei++;
         
#         else
#         {
           
#             int curr_length = ei - si;
         
#             if (curr_length < min_length) 
#             {
#                 min_length = curr_length;
#                 min_start_index = si;
#             }
          
# 	      ei++;
#           si=ei;
#         }
      
        
#     }
#  for(int i=0;i<min_length;i++)
#  {
#    output[i]=input[min_start_index++];
  
#  }

# }
