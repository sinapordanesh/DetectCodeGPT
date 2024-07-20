def minimum_cubes():
    while True:
        w, d = map(int, input().split())
        if w == 0 and d == 0:
            break
        front_view = list(map(int, input().split()))
        side_view = list(map(int, input().split()))
        front_heights = [max(front_view[:i+1]) for i in range(w)]
        side_heights = [max(side_view[:i+1]) for i in range(d)]
        total_cubes = sum(min(front_heights[i], side_heights[j]) for i in range(w) for j in range(d))
        print(total_cubes)

minimum_cubes()