def permutation(n):
    from itertools import permutations
    
    nums = [str(i) for i in range(1, n+1)]
    
    for perm in permutations(nums):
        print(' '.join(perm))

n = int(input())
permutation(n)