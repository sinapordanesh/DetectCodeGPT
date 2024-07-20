import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    n, *a = map(int, read().split())
    r = 0
    for i1, ae in enumerate(a):
        if (i1+1)&1 and ae&1:
            r += 1
    print(r)

if __name__ == '__main__':
    main()