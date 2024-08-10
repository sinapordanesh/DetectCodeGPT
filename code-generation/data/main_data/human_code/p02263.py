inputEnzan=input().split()

def keisan(inputEnzan):
    while True:
        stockFornumber=[]
        index=0
        length=len(inputEnzan)
        if length==1:
            break
        while index<length:
            if inputEnzan[index]=="+" or inputEnzan[index]=="-" or inputEnzan[index]=="*":
                if len(stockFornumber)==2:
                    if inputEnzan[index]=="+":
                        inputEnzan[index]=stockFornumber[0]+stockFornumber[1]
                        stockFornumber=[]
                        inputEnzan[index-1]="null"
                        inputEnzan[index-2]="null"

                    elif inputEnzan[index]=="-":
                        inputEnzan[index]=stockFornumber[0]-stockFornumber[1]
                        stockFornumber=[]
                        inputEnzan[index-1]="null"
                        inputEnzan[index-2]="null"

                    else:
                        inputEnzan[index]=stockFornumber[0]*stockFornumber[1]
                        stockFornumber=[]
                        inputEnzan[index-1]="null"
                        inputEnzan[index-2]="null"
                else:
                    stockFornumber=[]
                    pass

            else:
                if len(stockFornumber)==2:
                    del stockFornumber[0]
                stockFornumber.append(int(inputEnzan[index]))
                    
            index+=1

        while "null" in inputEnzan:
            inputEnzan.remove("null")

    print(inputEnzan[0])

keisan(inputEnzan)  
