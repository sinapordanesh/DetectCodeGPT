def evaluate_performance(scores):
    m, f, r = scores
    if m == -1 or f == -1:
        return "F"
    total = m + f
    if total >= 80:
        return "A"
    elif total >= 65:
        return "B"
    elif total >= 50:
        return "C"
    elif total >= 30:
        if r >= 50:
            return "C"
        else:
            return "D"
    else:
        return "F"

while True:
    scores = list(map(int, input().split()))
    if scores == [-1, -1, -1]:
        break
    print(evaluate_performance(scores))