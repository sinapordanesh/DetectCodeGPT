from sys import stdin
rs = lambda : stdin.readline().strip()
ri = lambda : int(rs())
ril = lambda : list(map(int, rs().split()))

def main():
    s = rs()
    if len(s) == 2:
        print(s)
    else:
        print(s[::-1])

if __name__ == '__main__':
    main()
