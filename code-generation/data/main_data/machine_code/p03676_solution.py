def subsequences(n, sequence):
    MOD = 10**9 + 7
    freq = [0] * (n+1)
    for num in sequence:
        freq[num] += 1
    
    result = [0] * (n+1)
    result[1] = 1
    
    for i in range(2, n+2):
        result[i] = (result[i-1] + ((pow(2, freq[i-1], MOD) - 1) * result[i-1]) % MOD) % MOD
    
    return result

n = int(input())
sequence = list(map(int, input().split()))
for res in subsequences(n, sequence):
    print(res)