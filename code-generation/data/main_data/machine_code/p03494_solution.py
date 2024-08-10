def max_operations(N, A):
    count = 0
    while all(x % 2 == 0 for x in A):
        A = [x // 2 for x in A]
        count += 1
    return count

N = int(input())
A = list(map(int, input().split()))

print(max_operations(N, A))