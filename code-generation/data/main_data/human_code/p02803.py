#!/usr/bin/env python3
def main():
    from collections import deque
    import numpy as np

    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    move = ((0, 1), (0, -1), (1, 0), (-1, 0))
    seen = [[False] * W for _ in range(H)]
    ans = 0
    for sh in range(H):
        for sw in range(W):
            if S[sh][sw] == '#' or seen[sh][sw]:
                continue
            seen[sh][sw] = True
            queue = deque([(sh, sw)])
            # distance = np.zeros((H, W), dtype=np.int16)
            distance = np.full((H, W), -1, dtype=np.int16)
            distance[sh, sw] = 0
            while queue:
                h, w = queue.popleft()
                for dh, dw in move:
                    nh = h + dh
                    nw = w + dw
                    if (1
                            and 0 <= nh < H
                            and 0 <= nw < W
                            and S[nh][nw] == '.'
                            and distance[nh][nw] == -1):
                        distance[nh][nw] = distance[h][w] + 1
                        queue.append((nh, nw))
            ans = max(ans, distance.max())
    print(ans)


if __name__ == '__main__':
    main()
