n, k = map(int, input().split())
d = list(map(int, input().split()))
ng = [False] * 10
for i in d:
    ng[i] = True
def ok(n):
    global ng
    while n > 0:
        if ng[n%10]:
            return False
        n //= 10
    return True
while not ok(n):
    n += 1
print(n)