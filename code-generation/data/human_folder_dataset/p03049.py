import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()


N = I()

ans = 0
b_start,a_end,b_start_a_end = 0,0,0
# Bで始まりAで終わらない文字列、Bで始まらずAで終わる文字列、Bで始まりAで終わる文字列の個数
for i in range(N):
    s = S()
    if s[0] == 'B' and s[-1] == 'A':
        b_start_a_end += 1
    elif s[0] == 'B':
        b_start += 1
    elif s[-1] == 'A':
        a_end += 1
    for j in range(len(s)-1):
        if s[j] == 'A' and s[j+1] == 'B':
            ans += 1

if b_start_a_end == 0:
    print(ans+min(b_start,a_end))
else:
    ans += b_start_a_end-1  # b_start_a_end == 1 として良い
    if a_end > 0:
        ans += 1
        a_end -= 1
    if b_start > 0:
        ans += 1
        b_start -= 1
    ans += min(b_start,a_end)
    print(ans)
