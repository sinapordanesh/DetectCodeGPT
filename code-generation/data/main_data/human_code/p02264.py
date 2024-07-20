#----------------for input------------------------
numberAndQuontum=input().split()
number=int(numberAndQuontum[0])
Quontum=int(numberAndQuontum[1])
allProcessList=[]

index=0
while index<number:
    nameAndTime=input().split()
    nameTimeList=[]
    nameTimeList.append(nameAndTime[0])
    nameTimeList.append(int(nameAndTime[1]))
    allProcessList.append(nameTimeList)
    index+=1
#----------------for input------------------------

def schedule(Quontum,allProcessList):
    time=0
    listForReturn=[]
    while True:
        index=0
        if allProcessList==[]:
            break
        length=len(allProcessList)
        while index<length:
            if allProcessList[index][1]<=Quontum:
                time+=allProcessList[index][1]
                listForReturn.append(allProcessList[index][0]+" "+str(time))
                allProcessList[index]=[]
                index+=1
            else:
                time+=Quontum
                listForAppend=[allProcessList[index][0],allProcessList[index][1]-Quontum]
                allProcessList.append(listForAppend)
                allProcessList[index]=[]
                index+=1
        while [] in allProcessList:
            allProcessList.remove([])
    for printPair in listForReturn:
        print(printPair)

#-------------------for main---------------------------
schedule(Quontum,allProcessList)

            

