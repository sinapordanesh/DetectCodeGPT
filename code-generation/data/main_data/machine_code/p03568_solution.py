def count_integer_sequences(N, A):
    count = 1
    for num in A:
        if num % 2 == 0:
            count *= 2
    return count

N = int(input())
A = list(map(int, input().split()))
print(count_integer_sequences(N, A))