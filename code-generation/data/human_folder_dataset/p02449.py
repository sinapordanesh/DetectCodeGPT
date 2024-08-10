import itertools

def print_elements(a):
    print(' '.join(list(map(str, a))))

n = int(input())
a = tuple(map(int, input().split(' ')))

permutations = list(itertools.permutations([i+1 for i in range(n)]))
for i, per in enumerate(permutations):
    if per == a:
        if i != 0: print_elements(permutations[i-1])
        print_elements(a)
        if i != len(permutations)-1: print_elements(permutations[i+1])
