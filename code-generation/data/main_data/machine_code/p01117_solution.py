def highest_total_score():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        scores = []
        for _ in range(m):
            scores.append(list(map(int, input().split())))
        
        max_total = 0
        for i in range(n):
            total = sum(scores[j][i] for j in range(m))
            if total > max_total:
                max_total = total
        
        print(max_total)

highest_total_score()