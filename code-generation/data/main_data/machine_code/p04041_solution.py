def haiku_sequences(N, X, Y, Z):
    MOD = 10**9 + 7

    count = 0
    for num in range(1, 11**N):
        sequence = []
        for i in range(N):
            sequence.append(num % 10)
            num //= 10
        
        for x in range(N):
            for y in range(x+1, N):
                for z in range(y+1, N):
                    for w in range(z+1, N):
                        if sum(sequence[x:y]) == X and sum(sequence[y:z]) == Y and sum(sequence[z:w]) == Z:
                            count += 1
                            count %= MOD

    return count

# Sample Input
print(haiku_sequences(3, 5, 7, 5))
print(haiku_sequences(4, 5, 7, 5))
print(haiku_sequences(37, 4, 2, 3))
print(haiku_sequences(40, 5, 7, 5))