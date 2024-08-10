MOD = 10**9 + 7

def sum_of_beauty(N, M, marks):
    ans = 1
    prev = 0
    
    for mark in marks:
        length = mark - prev - 1
        ans = (ans * (length * length + 1)) % MOD
        prev = mark
    
    length = N - prev
    ans = (ans * (length * length + 1)) % MOD
    
    return ans

N, M = map(int, input().split())
marks = [int(x) for x in input().split()]

print(sum_of_beauty(N, M, marks))