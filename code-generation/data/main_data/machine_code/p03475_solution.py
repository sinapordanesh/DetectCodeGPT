def main():
    N = int(input())
    trains = [list(map(int, input().split())) for _ in range(N-1)]

    for i in range(N):
        time = 0
        for j in range(i, N-1):
            C, S, F = trains[j]
            if time < S:
                time = S
            elif time % F == 0:
                pass
            else:
                time += F - (time % F)
            time += C
        print(time)

if __name__ == "__main__":
    main()