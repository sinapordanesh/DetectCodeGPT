def main():
    import sys
    import numpy as np
    ikimasu = sys.stdin.buffer.readline
    ini = lambda: int(ins())
    ina = lambda: list(map(int, ikimasu().split()))
    ins = lambda: ikimasu().strip()
    
    n = ini()
    tmp = ina()
    num,index = 0,0
    for i in range(n):
        if(abs(tmp[i])>num):
            num,index = abs(tmp[i]),i
    print(2*n-2)
    if(tmp[index]<=0):
        for i in range(n):
            if(i!=index):
                print(index+1,i+1)
        for i in range(n,1,-1):
            print(i,i-1)
    else:
        for i in range(n):
            if(i!=index):
                print(index+1,i+1)
        for i in range(1,n):
            print(i,i+1)


        
        
        


    
        


        


    




















if __name__ == "__main__":
    main()
