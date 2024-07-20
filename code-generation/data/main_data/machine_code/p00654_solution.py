def squid_multiplication(n, sequence):
    even_num = min(sequence)
    odd_nums = [x for x in sequence if x % 2 != 0]
    odd_nums.sort()
    
    print(even_num)
    print(' '.join(map(str, odd_nums)))

# Input reading and function call
while True:
    n = int(input())
    if n == 0:
        break
    sequence = list(map(int, input().split()))
    squid_multiplication(n, sequence)