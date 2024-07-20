MOD = 1000000007
def count_occurrences(A, B, C):
    count = 0
    for i in range(A, B+1):
        count += str(i).count(str(C))
    return count % MOD

A, B, C = map(int, input().split())
print(count_occurrences(A, B, C))