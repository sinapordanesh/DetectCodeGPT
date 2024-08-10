def calculate_score():
    while True:
        n = int(input())
        if n == 0:
            break
        scores = [int(input()) for _ in range(n)]
        scores.sort()
        scores = scores[1:-1]
        avg_score = sum(scores) // len(scores)
        print(avg_score)

calculate_score()