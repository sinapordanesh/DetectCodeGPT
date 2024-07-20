def drop(lst,h,w):
    for i in range(w-1,-1,-1):
        work=[lst[j][i] for j in range(h)]
        work=[x for x in work if x]
        for j in range(h-1,-1,-1):
            if work: lst[j][i]=work.pop()
            else : lst[j][i]=None

def chain(lst,h,w,k):
    sm=0
    for j in range(h):
        train=1
        for i in range(w-1):
            if not lst[j][i] :
                train=1
                continue
            if lst[j][i]==lst[j][i+1]:
                train+=1
            else :
                if train>=k:
                    sm+=lst[j][i]*train
                    lst[j][i-train+1:i+1]=[None]*train
                train=1
        if train>=k:
            sm+=lst[j][-1]*train
            lst[j][-train:]=[None]*train
    return sm


def procedure(lst,h,w,k,x):
    lst[x[0]][x[1]]=None
    drop(lst,h,w)
    sm=0
    i=0
    point=chain(lst,h,w,k)
    while point:
        sm+=(2**i)*point
        drop(lst,h,w)
        point=chain(lst,h,w,k)
        i+=1
        #print(lst)
    return sm


def main():
    h,w,k=map(int,input().split())
    lst=[[int(x) for x in input()] for _ in range(h)]
    mx=0

    for i in range(1,h):
        for j in range(w):
            work=[[lst[i][j] for j in range(w)] for i in range(h)]
            sm=procedure(work,h,w,k,(i,j))
            if mx<sm : mx=sm
    print(mx)


main()