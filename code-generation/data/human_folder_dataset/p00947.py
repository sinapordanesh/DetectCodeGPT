import copy
T = [[int(x) for  x in input().split()] for i in range(10)]

def E(ID):
#    if len(ID)!=4:
    #    print(len(ID))
    ret = 0
    for d in ID:
        d  =int(d)
        ret = T[ret][d]
    return ret

def solve(ID):
    e = E(ID)
    for i in range(4):
        for j in range(10):
            kari = copy.deepcopy(ID)
            if kari[i] == str(j):
                continue
            kari[i] = str(j)
            if T[E(kari)][e]==0:
                return 1
    for i in range(10):
        if T[E(ID)][i] == 0 and i!=e:
            return 1
    for i in range(3):
        kari = copy.deepcopy(ID)
        if kari[i] == kari[i+1]:
            continue
        kari[i],kari[i+1] =kari[i+1],kari[i]
        if T[E(kari)][e]==0:
            return 1
    if T[E(ID[:3]+[str(e)])][int(ID[3])]==0 and int(ID[3])!=e:

        return 1
    #print(ID ,e)
    return 0
ans = 0
for i in range(10000):
    ID  =[j for j in str(i)]
    ID = ['0']*(4-len(ID)) + ID
    ans += solve(ID)

print(ans)


