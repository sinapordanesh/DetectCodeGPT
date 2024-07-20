def calc_tairyoku(x, p):
    return (x - p) ** 2

N = int(input())
X = list(map(int, input().split()))
X = sorted(X)
min_x = X[0]
max_x = X[N-1]

result = 10 ** 6
for x in range(min_x, max_x+1):
    s = sum([calc_tairyoku(x, i) for i in X])
    result = min(result, s)

print(result)
    
