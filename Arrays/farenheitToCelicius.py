def printTable(fs,fe,step):
    i = fs
    while(fe >= i):
        c = (i - 32)*(5/9)
        c = int(c)
        print(i,c)
        i = i + step

fs = int(input())
fe = int(input())
step = int(input())
printTable(fs,fe,step)