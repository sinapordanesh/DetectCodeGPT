def reachable_destination(N, D, d, Q, q):
    result = []
    for i in range(Q):
        if sum(d[:q[i]]) >= D:
            result.append("NO")
        else:
            result.append("YES")
    return result

N, D = map(int, input().split())
d = list(map(int, input().split()))
Q = int(input())
q = list(map(int, input().split()))

for res in reachable_destination(N, D, d, Q, q):
    print(res)