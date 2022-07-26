
def highestOccuringCharacter(string):
    
    hashMap = {} # key : value => character in the string : count of occurance
    
    for i in string:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1
    
    res = max(hashMap, key = hashMap.get)
    print(res)

string = "acccbbaba"
highestOccuringCharacter(string)
def highestOccuringChar(string):

    n = len(string)
    frequency = [0] * 256
    countS = 0

    for i in range(n):
        frequency[ord(string[i])] += 1
        countS = max(countS, frequency[ord(string[i])])
    
    answer = '\0'

    for i in range(n):
        if frequency[ord(string[i])] == countS:
            answer = string[i]
            break

    print (answer)
    highestOccuringChar(string)
