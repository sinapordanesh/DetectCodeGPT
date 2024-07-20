import sys
from bisect import bisect_left

def main():
    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    n = int(input())
    ruins = [list(map(int, input().split())) for _ in range(n)]
    ruins.sort(key=lambda x: (x[1], x[0]))

    x_coords = [r[0] for r in ruins]
    cumulative_x = [0]
    for x in x_coords:
        cumulative_x.append(cumulative_x[-1] + x)

    total_cost = float('inf')
    for i in range(1, n):
        x_line = ruins[i][0]
        west_ruins = cumulative_x[i]
        east_ruins = cumulative_x[-1] - cumulative_x[i]

        west_cost = 0
        east_cost = 0

        min_cost = float('inf')
        for j in range(n):
            cost = abs(ruins[j][0] - x_line) + ruins[j][1]
            min_cost = min(min_cost, cost)

        west_cost += west_ruins - min_cost

        min_cost = float('inf')
        for j in range(n):
            cost = abs(ruins[j][0] - x_line) + ruins[j][1]
            min_cost = min(min_cost, cost)

        east_cost += east_ruins - min_cost

        total_cost = min(total_cost, west_cost + east_cost)

    print(round(total_cost))

if __name__ == "__main__":
    main()