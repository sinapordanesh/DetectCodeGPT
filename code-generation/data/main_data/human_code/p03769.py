def test():
    from itertools import combinations

    s = '111223111223'
    result = 0
    for k in range(1, len(s) // 2 + 1):
        for idx in combinations(range(len(s)), 2 * k):
            success = True
            for ii in range(k):
                if s[idx[ii]] != s[idx[ii + k]]:
                    success = False
                    break
            if success:
                result += 1
    print(result)


n = int(input())

factorials = [1, 1]
for i in range(2, 40):
    factorials.append(factorials[-1] * i)

patterns = {}
for i in range(2, 40):
    base = (1 << (i - 1)) - 1
    gain = base
    chars = i
    if gain > n:
        break
    if gain not in patterns or chars < patterns[gain][0]:
        patterns[gain] = (chars, (i,))
    if i % 2 == 1:
        continue

    a = i // 2
    ncr1 = factorials[i] // factorials[a] // factorials[a] - 1

    for b in range(1, a + 1):
        base2 = (1 << (2 * b - 1)) - 1
        ncr2 = factorials[2 * b] // factorials[b] // factorials[b] - 1
        gain = base + base2 + ncr1 * ncr2
        chars = i + 2 * b
        if gain > n:
            break
        if gain not in patterns or chars < patterns[gain][0]:
            patterns[gain] = (chars, (a, b))

        for c in range(1, b + 1):
            base3 = (1 << (2 * c - 1)) - 1
            ncr3 = factorials[2 * c] // factorials[c] // factorials[c] - 1
            gain = base + base2 + base3 + ncr1 * ncr2 * ncr3 + ncr1 * ncr2 + ncr2 * ncr3 + ncr3 * ncr1
            chars = i + 2 * b + 2 * c
            if gain > n:
                break
            if gain not in patterns or chars < patterns[gain][0]:
                patterns[gain] = (chars, (a, b, c))

            for d in range(1, c + 1):
                base4 = (1 << (2 * d - 1)) - 1
                ncr4 = factorials[2 * d] // factorials[d] // factorials[d] - 1
                gain = base + base2 + base3 + base4 + ncr1 * ncr2 * ncr3 * ncr4
                gain += ncr1 * ncr2 * ncr3 + ncr1 * ncr2 * ncr4 + ncr1 * ncr3 * ncr4 + ncr2 * ncr3 * ncr4
                gain += ncr1 * ncr2 + ncr1 * ncr3 + ncr1 * ncr4 + ncr2 * ncr3 + ncr2 * ncr4 + ncr3 * ncr4
                chars = i + 2 * b + 2 * c + 2 * d
                if gain > n:
                    break
                if gain not in patterns or chars < patterns[gain][0]:
                    patterns[gain] = (chars, (a, b, c, d))


def dfs(use, i, remaining, total_char):
    if remaining == 0:
        return total_char <= 200

    for j in range(i, len(patterns)):
        gain, (chars, lengths) = patterns[j]
        if total_char + remaining * chars / gain > 200:
            break
        if gain > remaining:
            continue
        use.append(lengths)
        result = dfs(use, j, remaining - gain, total_char + chars)
        if result:
            return True
        use.pop()

    return False


patterns = sorted(patterns.items(), key=lambda item: item[0] / item[1][0], reverse=True)

use = []
result = dfs(use, 0, n, 0)
assert result

ans = []
c = 1
for lengths in use:
    if len(lengths) == 1:
        ans.extend([c] * lengths[0])
        c += 1
    else:
        for _ in range(2):
            for i, l in enumerate(lengths):
                ans.extend([c + i] * l)
        c += len(lengths)

print(len(ans))
print(*ans)
