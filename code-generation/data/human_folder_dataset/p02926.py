from math import atan2, sqrt

def main():
    n = int(input())
    engines = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        rad = atan2(engines[i][1], engines[i][0])
        engines[i].append(rad)
    engines.sort(key=lambda x: x[2])
    ans = 0
    for k in range(1, n+1):
        for i in range(n):
            x_sum, y_sum = 0, 0
            for j in range(i, i+k):
                p = j%n
                x_sum += engines[p][0]
                y_sum += engines[p][1]
            tmp = x_sum**2 + y_sum**2
            if ans < tmp:
                ans = tmp
    print(sqrt(ans))

if __name__ == "__main__":
    main()