from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    s = rs()
    ans = s.count('2')
    print(ans)

if __name__ == '__main__':
    main()
