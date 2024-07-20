from collections import defaultdict, deque


def main():
    N, M = list(map(int, input().split()))
    adj = defaultdict(list)
    A, B = -1, -1
    for _ in range(M):
        A, B = list(map(lambda x: int(x) - 1, input().split()))
        adj[A].append(B)
        adj[B].append(A)

    visited = [0] * N
    visited[A] = 1
    visited[B] = 1
    from_a = list()
    que = deque([A])
    while len(que) > 0:
        n = que.pop()
        from_a.append(n)
        visited[n] = 1
        all_visited = True
        for next_n in adj[n]:
            if visited[next_n] == 1:
                continue
            que.append(next_n)
            all_visited = False
        if all_visited:
            break
    from_b = list()
    que = deque([B])
    while len(que) > 0:
        n = que.pop()
        from_b.append(n)
        visited[n] = 1
        all_visited = True
        for next_n in adj[n]:
            if visited[next_n] == 1:
                continue
            que.append(next_n)
            all_visited = False
        if all_visited:
            break
    ans = from_a[::-1] + from_b
    ans = [x + 1 for x in ans]
    print(len(ans))
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
