def max_smaller_scores(Q, queries):
    def calculate_score(rank1, rank2):
        return rank1 * rank2

    def count_smaller_scores(T_rank1, T_rank2, participants):
        T_score = calculate_score(T_rank1, T_rank2)
        count = 0
        for participant in participants:
            if calculate_score(participant[0], participant[1]) < T_score:
                count += 1
        return count

    for query in queries:
        print(count_smaller_scores(query[0], query[1], [(i, j) for i in range(1, 10**10+1) for j in range(1, 10**10+1)]))

# Sample Input
max_smaller_scores(8, [(1, 4), (10, 5), (3, 3), (4, 11), (8, 9), (22, 40), (8, 36), (314159265, 358979323)])