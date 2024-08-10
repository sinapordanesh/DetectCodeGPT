import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    NI = lambda : int(sys.stdin.readline())

    N = NI()

    a = []
    for i in range(3,30001):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            a.append(i)

    ans = []
    s = 0
    for x in a[:N-2]:
        ans.append(x)
        s += x
    i = N-2
    while (s + a[i]) % 2:
        i += 1
    ans.append(a[i])
    s += a[i]

    i += 1
    while (s + a[i]) % 30 > 0:
        i += 1
    ans.append(a[i])

    print(*ans)

if __name__ == '__main__':
    main()