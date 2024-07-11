x = int(input())
ans = 0
def f(n):return((n* (n+1))//2)
while f(ans) < x:
    ans += 1
print(ans)