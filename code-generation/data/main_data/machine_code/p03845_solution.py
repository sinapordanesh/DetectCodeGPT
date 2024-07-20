def calculate_solve_time():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    drinks = []
    for _ in range(M):
        drinks.append(list(map(int, input().split())))

    for drink in drinks:
        total_time = sum(T)
        total_time -= T[drink[0]-1]
        total_time += drink[1]
        print(total_time)

calculate_solve_time()