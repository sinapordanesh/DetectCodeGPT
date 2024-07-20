def main():
    N, M, K = map(int, input().split())
    A, B, C = map(int, input().split())
    T = int(input())
    express_stops = [int(input()) for _ in range(M)]

    def possible_stations(time):
        express_time = (express_stops[-1] - 1) * B
        if express_time > time:
            return -1
        time -= express_time
        possible = min(N - 1, (time // A) + 1)
        return possible

    left = 0
    right = T
    while left < right:
        mid = (left + right + 1) // 2
        if possible_stations(mid * C) >= K:
            left = mid
        else:
            right = mid - 1

    print(left)

if __name__ == "__main__":
    main()