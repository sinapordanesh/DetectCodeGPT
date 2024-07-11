def main():
    import sys
    import numpy as np
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    
    n,m,q = ina()
    tmp = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        l,r = ina()
        tmp[l][r]+=1


    tmp = np.cumsum(tmp,axis=1).cumsum(axis = 0)

    for _ in range(q):
        p,q = ina()
        rick = tmp[q][q]+tmp[p-1][p-1]-tmp[p-1][q]-tmp[q][p-1]
        print(rick)
        


    
        


        


    




















if __name__ == "__main__":
    main()
