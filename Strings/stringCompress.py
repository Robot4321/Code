def stringCompression(str1):
    
    res = ""
    count = 1
    for i in range(len(str1) - 1):
        if str1[i] == str1[i+1]:
            count = count + 1 
        else:
            res += str1[i] + str(count)
            count = 1
    res += str1[i] + str(count)
    
    print(res)  


str1 = "aaaabbbbccccddddaaaayyyyaa"
stringCompression(str1)