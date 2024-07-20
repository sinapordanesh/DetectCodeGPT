def main():
    import sys
    sys.setrecursionlimit(311111)
    # import numpy as np
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    n,k = ina()
    tmp = ina()
    x = 1<<55
    rick = 0
    used = 0
    for _ in range(55+1):
        tmp1 = 0
        for i in tmp:
            if(i&x):
                tmp1+=1
        if(tmp1>=(n-tmp1)):
            rick+=x*tmp1
        else:
            if((x+used<=k)):
                rick+=x*(n-tmp1)
                used +=x
            else:
                rick+=x*tmp1
        x>>=1
    print(rick)


    


        
        
        


    
        


        


    




















if __name__ == "__main__":
    main()
