import itertools

def print_elements(a):
    print(' '.join(list(map(str, a))))

n = int(input())
for per in list(itertools.permutations([i+1 for i in range(n)])):
    print_elements(per)
