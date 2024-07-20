from collections import deque
from collections import defaultdict

def main():
    N, X, Y = map(int, input().split())
    graph = [[] for _ in range(N)]
    graph[X-1].append(Y-1)
    graph[Y-1].append(X-1)
    for i in range(N-1):
        graph[i].append(i+1)
        graph[i+1].append(i)

    dist_freq = defaultdict(int)
    for start in range(N):
        d = deque([start])
        distance = [-1] * N
        distance[start] = 0
        while d:
            current_node = d.popleft()
            for next_node in graph[current_node]:
                if distance[next_node] == -1:
                    distance[next_node] = distance[current_node] + 1
                    d.append(next_node)
        for v in distance:
            if v != 0:
                dist_freq[v] += 1
    for k in range(1, N):
        print(dist_freq[k] // 2)


if __name__ == '__main__':
    main()
