n = int(input())
p = [item for sublist in [[int(input().split()[1])] if i != 0 else list(map(int, input().split())) for i in range(n)] for item in sublist]

def memolize(f):
    cache = {}

    def helper(x, y):
        if (x, y) not in cache:
            cache[(x, y)] = f(x, y)
        return cache[(x, y)]
    return helper

@memolize
def calcMatrixOrder(i, j):
    if i == j :
        return 0
    return min([calcMatrixOrder(i, k) + calcMatrixOrder(k + 1, j) + p[i]*p[k+1]*p[j + 1] for k in range(i, j)])

print(calcMatrixOrder(0, n - 1))

