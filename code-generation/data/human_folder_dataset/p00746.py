def main():
    D = ((-1,0), (0,-1), (1,0), (0,1))
    while True:
        n = int(input())
        if n==0:
            exit()
        sx = [0]
        sy = [0]

        for i in range(n-1):
            ni, di = [int(x) for x in input().split()]
            sx.append(sx[ni]+D[di][0])
            sy.append(sy[ni]+D[di][1])
        w = max(sx)-min(sx)+1
        h = max(sy)-min(sy)+1
        print(w,h)

if __name__ == '__main__':
    main()