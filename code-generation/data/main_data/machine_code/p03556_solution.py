import math

def largest_square_number(N):
    return int(math.sqrt(N)) ** 2

N = int(input())
print(largest_square_number(N))