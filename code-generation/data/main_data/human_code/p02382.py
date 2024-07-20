import math
def main():

    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))    

    print(Minkowski(n, x, y, 1))
    print(Minkowski(n, x, y, 2))
    print(Minkowski(n, x, y, 3))
    print(Chebyshev(n, x, y))


def Minkowski(n, x, y, p):
    temp = 0
    for i in range(n):
        temp += abs(y[i] - x[i])**p
    return temp**(1/p)

def Chebyshev(n, x, y):
    temp = 0
    for i in range(n):
        temp = max(temp, abs(y[i] - x[i]))
    return temp

if __name__ == '__main__':
    main()


