def check(l, r):
    th = 1 + (r - l + 1) // 2 
    for i in range(26):
        if cnt[i] >= th:
            return True
    return False

s = input()
n = len(s)
si = [0] * n
for i in range(n):
    si[i] = ord(s[i]) - 97

l, r = 0, 1
cnt = [0]*26
for i in range(2):
    cnt[si[i]] += 1
while l < n-1 and r < n:
    if check(l, r):
        print(l+1, r+1)
        exit()
    elif max(cnt) == 1 + (r - l + 1) // 2 or r-l == 1:
        r += 1
        if r < n:
            cnt[si[r]] += 1
    else:
        cnt[si[l]] -= 1
        l += 1     
print(-1, -1)