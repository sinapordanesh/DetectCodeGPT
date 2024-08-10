from collections import Counter
from itertools import product, permutations
def main():
    n, c = map(int, input().split())
    D = [list(map(int, input().split())) for _ in range(c)]
    C = [list(map(lambda x:int(x)-1, input().split())) for _ in range(n)]

    group = [Counter([C[i][j] for i,j in product(range(n), range(n)) if (i+j+2) %3 == k]) for k in range(3)] 
    
    ans = float('inf')
    for color in permutations(range(c), 3):
        diff = 0
        for i in range(3):
            diff += sum(D[before_color][color[i]]*count for before_color, count in group[i].items())
        ans = min(ans, diff)
    print(ans)

main()