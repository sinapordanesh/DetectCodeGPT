mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    A = input().rstrip('\n')
    B = input().rstrip('\n')
    N = len(A)

    if A == B:
        print(0)
        exit()
    if int(B) == 0:
        print(-1)
        exit()

    def solve(A, B):
        left = [0] * N
        right = [0] * N
        for i in range(N):
            for j in range(N):
                if B[(i-j)%N] == "1":
                    left[i] = j
                    break
        for i in range(N):
            for j in range(N):
                if B[(i+j)%N] == "1":
                    right[i] = j
                    break
        ret = 10**9
        for k in range(N):
            f = 0
            i_list = []
            for i in range(N):
                if A[i] != B[(i-k)%N]:
                    f += 1
                    i_list.append(i)
            lr = [0] * N
            lmax = 0
            rmax = 0
            for i in i_list:
                if left[i] <= k:
                    continue
                lr[left[i] - k] = max(lr[left[i] - k], right[i])
                lmax = max(lmax, left[i] - k)
            ret = min(ret, f + 2 * lmax + k)
            for l in range(N-1, 0, -1):
                rmax = max(rmax, lr[l])
                ret = min(ret, f + 2 * (l - 1 + rmax) + k)
        return ret
    print(min(solve(A, B), solve(A[::-1], B[::-1])))


if __name__ == '__main__':
    main()
