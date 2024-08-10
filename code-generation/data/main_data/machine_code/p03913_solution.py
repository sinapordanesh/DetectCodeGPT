def shortest_time_to_produce(N, A):
    cookies = 0
    time = 0
    production_rate = 1
    
    while cookies < N:
        if cookies >= A:
            time += (N - cookies + production_rate - 1) // production_rate
            break
        
        if cookies + production_rate + A <= N:
            time += A + 1
            production_rate += 1
            cookies += production_rate
        else:
            time += (N - cookies + production_rate - 1) // production_rate
            break
    
    return time

N, A = map(int, input().split())
print(shortest_time_to_produce(N, A))