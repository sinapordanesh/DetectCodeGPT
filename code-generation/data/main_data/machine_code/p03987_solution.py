def find_permutation_sum():
    N = int(input())
    a = list(map(int, input().split()))
    total_sum = sum(a)
    result = N*(N+1)//2 + total_sum
    print(result)

find_permutation_sum()