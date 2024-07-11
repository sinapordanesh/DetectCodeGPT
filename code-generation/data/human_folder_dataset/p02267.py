#---------------for input--------------------
numberN=int(input())
arrayS=list(map(int,input().split()))

numberQ=int(input())
arrayT=list(map(int,input().split()))
#---------------for input----------------------

def linearSearch(arrayS,arrayT,numberQ):
    machedNumber=0
    index=0
    while index<numberQ:
        if arrayT[index] in arrayS:
            machedNumber+=1
        index+=1
    print(machedNumber) 

#----------------for main------------------------
linearSearch(arrayS,arrayT,numberQ)
#----------------for main------------------------
