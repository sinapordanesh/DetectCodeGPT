def count_integer_sequences(N):
    MOD = 10**9 + 7
    return (10**N - 2 * 9**N + 8**N) % MOD

# Test the function with sample inputs
print(count_integer_sequences(2))
print(count_integer_sequences(1))
print(count_integer_sequences(869121))