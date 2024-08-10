def maximum_sum_sequence():
    while True:
        n = int(input())
        if n == 0:
            break
        sequence = [int(input()) for _ in range(n)]
        max_sum = sequence[0]
        current_sum = sequence[0]
        for i in range(1, n):
            current_sum = max(sequence[i], current_sum + sequence[i])
            max_sum = max(max_sum, current_sum)
        print(max_sum)

maximum_sum_sequence()