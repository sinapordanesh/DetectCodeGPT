def find_permutation_difference():
    import itertools
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    
    a = list(itertools.permutations(range(1, N+1))).index(tuple(P)) + 1
    b = list(itertools.permutations(range(1, N+1))).index(tuple(Q)) + 1
    
    print(abs(a - b))

find_permutation_difference()