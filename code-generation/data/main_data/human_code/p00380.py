
def solve():
    N = int(input())
    a = [int(i) for i in input().split()]
    Q = int(input())
    sort_a = sorted(a)
    judge = 0
    for i in range(N):
        if a[i] != sort_a[i]:
            judge += 1
    if judge == 0:
        print(0)
    else:
        for i in range(Q):
            x, y = map(int, input().split())
            tmp = a[x - 1]
            a[x - 1] = a[y - 1]
            a[y - 1] = tmp
            if a[x - 1] == sort_a[x - 1] and a[y - 1] != sort_a[x - 1]:
                judge -= 1
            if a[x - 1] != sort_a[x - 1] and a[y - 1] == sort_a[x - 1]:
                judge += 1
            if a[y - 1] == sort_a[y - 1] and a[x - 1] != sort_a[y - 1]:
                judge -= 1
            if a[y - 1] != sort_a[y - 1] and a[x - 1] == sort_a[y - 1]:
                judge += 1
            if judge == 0:
                print(i + 1)
                break
        else:
            print(-1)


if __name__ == '__main__':
    solve()
