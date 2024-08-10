import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import accumulate
def main():
    n, k = map(int, input().split())
    p = tuple(map(int, input().split()))
    c = tuple(map(int, input().split()))

    if k == 1:
        print(max(c))
        sys.exit()
    seen = [0] * n
    cycles = []
    for i1 in range(n):
        if not seen[i1]:
            cycle_t = []
            koko = i1
            while True:
                if seen[koko]:
                    cycles.append(cycle_t)
                    break
                cycle_t.append(c[koko])
                seen[koko] = 1
                koko = p[koko] - 1

    score = max(c)
    for cycle in cycles:
        score_t = max(cycle)
        cycle_len = len(cycle)
        cycle_sum = sum(cycle)
        kaisu, rem = divmod(k, cycle_len)
        if rem == 0:
            kaisu -= 1
            rem = cycle_len
        if kaisu > 0:
            kaisu -= 1
            rem += cycle_len
        cycle = tuple(accumulate(cycle + cycle + cycle))
        for i1 in range(2, rem + 1):
            for i2 in range(cycle_len):
                score_t = max(score_t, cycle[i1+i2] - cycle[i2])
        if cycle_sum > 0:
            score_t += (kaisu * cycle_sum)
        score = max(score, score_t)
    print(score)

if __name__ == '__main__':
    main()
