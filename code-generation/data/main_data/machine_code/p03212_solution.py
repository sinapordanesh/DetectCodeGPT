def shichi_go_san_numbers(N):
    count = 0
    for i in range(1, N+1):
        num_str = str(i)
        if '7' in num_str and '5' in num_str and '3' in num_str and set(num_str) <= {'7', '5', '3'}:
            count += 1
    return count

N = int(input())
print(shichi_go_san_numbers(N))