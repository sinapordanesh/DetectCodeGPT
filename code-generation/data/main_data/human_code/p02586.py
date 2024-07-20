from copy import deepcopy

def getval():
    r,c,k = map(int,input().split())
    item = [[0 for i in range(c)] for i in range(r)]
    for i in range(k):
        ri,ci,vi = map(int,input().split())
        item[ri-1][ci-1] = vi
    return r,c,k,item

def main(r,c,k,item):
    #DP containing the information of max value given k items picked in i,j
    prev = [[0 for i in range(4)]]
    inititem = item[0][0]
    prev[0] = [0,inititem,inititem,inititem]
    for i in range(1,r):
        initval = prev[i-1][3]
        temp = []
        cur = item[i][0]
        for j in range(4):
            temp.append(initval)
        for j in range(1,4):
            temp[j] += cur
        prev.append(temp)

    for j in range(1,c):
        init = deepcopy(prev[0])
        for i in range(1,4):
            init[i] = max(prev[0][i],prev[0][i-1]+item[0][j])
        curcol = [init]
        for i in range(1,r):
            cur = item[i][j]
            left = curcol[-1]
            down = prev[i]
            temp = [max(left[3],down[0])]
            for k in range(1,4):
                temp.append(max(max(left[3],down[k-1])+cur,down[k]))
            curcol.append(temp)
        prev = curcol
            
    print(max(prev[-1]))
           
if __name__=="__main__":
    r,c,k,item = getval()
    main(r,c,k,item) 