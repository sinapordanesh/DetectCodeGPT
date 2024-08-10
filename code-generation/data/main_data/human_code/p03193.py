from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    N, H, W = ril()
    ans = 0
    for i in range(N):
        a, b = ril()
        if H <= a and W <= b:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
