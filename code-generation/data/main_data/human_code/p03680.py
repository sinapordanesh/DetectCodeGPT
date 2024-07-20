
def resolve():
    N = int(input())
    A = [ int(input()) for _ in range(N)]

    #print(N, A)

    next = 0
    cnt = 0
    for i in range(N):
        next = A[next] - 1
        #print(next)
        cnt += 1
        if next == 1:
            break

    if cnt == N:
        print(-1)
    else:
        print(cnt)


if __name__ == "__main__":
    resolve()