n = int(input())
a = list(map(int, input().split()))
def f(x):
    b = '0' * 64 + bin(x)[2:]
    b = b[::-1]
    b = b[:64]
    return list(map(int, list(b)))

bit_count = [0] * 64
for i in a:
    b = f(i)
    for j in range(64):
        bit_count[j] += b[j]

ans = 0
for i in range(64):
    bc = bit_count[i]
    ans += (2**i) * bc * (n - bc)
    ans %= 10**9 + 7

print(ans)