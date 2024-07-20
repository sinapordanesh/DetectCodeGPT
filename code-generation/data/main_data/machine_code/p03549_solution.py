import math

def expected_total_execution_time(N, M):
    total_time = 0
    for i in range(1, M+1):
        total_time += (i * 1900 * (1/2)**i)
    for i in range(M+1, N+1):
        total_time += (i * 100 * (1/2)**M)
    return math.floor(total_time)

# Read input from stdin
N, M = map(int, input().split())

# Calculate and print the expected total execution time
print(expected_total_execution_time(N, M))