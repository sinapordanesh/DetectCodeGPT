def select_students(scores):
    scores.sort()
    min_diff = float('inf')
    for i in range(len(scores) - 1):
        diff = abs(scores[i] - scores[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff

while True:
    n = int(input())
    if n == 0:
        break
    scores = list(map(int, input().split()))
    print(select_students(scores))