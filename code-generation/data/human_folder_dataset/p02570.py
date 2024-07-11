import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

def main():
    d, t, s = map(int, input().split())
    if t * s >= d:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
