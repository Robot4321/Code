
def replaceCharacterInString(string,target, rep):
    res=""
    for i in string:
        if i != target:
            res += i
        else:
            res += rep

    print (res)

    if len(string) == len(res):
        print("Done")
    else:
        print("Not Done")






string = "aabbiiccssxxxxxx"
target = 'x'
rep = 'o'
replaceCharacterInString(string,target,rep)
