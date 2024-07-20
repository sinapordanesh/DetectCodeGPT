X,N=map(int,input().split())
p=input()
def ans170(X:int, N:int, p:str):
    p_list=list(map(int,p.split()))
    count=1
    if len(p)==0:
        return X
    elif X not in p_list:
        return X
    else:
        while True:
            if X-count not in p_list:
                return X-count
                break
            elif X+count not in p_list:
                return X+count
                break
            else:
                count+=1
print(ans170(X,N,p))
