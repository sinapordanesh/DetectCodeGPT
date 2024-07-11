# coding: utf-8


def main():
    N, M = map(int, input().split())
    ans = [0, 0]
    A = [[0, 0] for _ in range(N)]

    for i in range(M):
        p, s = input().split()
        p = int(p)
        if s == 'AC':
            A[p - 1][1] = 1
        elif A[p - 1][1] == 0:
            A[p - 1][0] += 1
    
    for i, j in A:
        if j == 1:
            ans[0] += 1
            ans[1] += i

    print(ans[0], ans[1])

if __name__ == "__main__":
    main()
