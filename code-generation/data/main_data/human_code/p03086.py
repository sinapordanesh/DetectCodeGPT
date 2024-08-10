import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
def main():
    s = tuple(input())
    r = 0
    s_len = len(s)
    for i1 in range(s_len):
        for i2 in range(i1 + 1, s_len + 1):
            if all([c in ('A', 'T', 'C', 'G') for c in s[i1:i2]]):
                r = max(r, i2 - i1)
    print(r)

if __name__ == '__main__':
    main()