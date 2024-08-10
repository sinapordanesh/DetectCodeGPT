import math

def standard_deviation(scores):
    n = len(scores)
    avg = sum(scores) / n
    variance = sum((x - avg) ** 2 for x in scores) / n
    std_dev = math.sqrt(variance)
    return std_dev

while True:
    n = int(input())
    if n == 0:
        break
    scores = list(map(int, input().split()))
    result = standard_deviation(scores)
    print("{:.10f}".format(result))