from collections import Counter
from itertools import combinations, starmap
func = lambda x, y, z: x*y*z

def main():
    with open(0) as f:
        N, *S = f.read().split()
    S = [s[0] for s in S if s[0] in list('MARCH')]
    S = Counter(S)
    ans = sum(starmap(func, combinations(S.values(), 3)))
    print(ans)

main()