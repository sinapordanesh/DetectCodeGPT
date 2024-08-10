
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def count_loop(start, idx_map):
    count = 0
    idx = start
    while True:
        idx = idx_map[idx]
        count += 1
        if idx == 0:
            break
    return count


A, B = zip(*sorted(zip(A, B), key=lambda x: x[1]))
idx_map = sorted(range(N), key=lambda i: A[i])
A = sorted(A)

check_1 = all(A[i] <= B[i] for i in range(N))
check_2 = any(A[i + 1] <= B[i] for i in range(N - 1))
check_3 = count_loop(0, idx_map) <= N - 2

if check_1 and (check_2 or check_3):
    print("Yes")
else:
    print("No")
