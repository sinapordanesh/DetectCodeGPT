def max_kupc(N, K, problems):
    from collections import Counter
    
    problem_letters = set()
    problem_count = Counter()
    
    for problem in problems:
        problem_letters.add(problem[0])
        problem_count[problem[0]] += 1
    
    max_kupc = min(K, len(problem_letters))
    
    return max_kupc

# Sample Input 1
print(max_kupc(9, 3, ["APPLE", "ANT", "ATCODER", "BLOCK", "BULL", "BOSS", "CAT", "DOG", "EGG"]))

# Sample Input 2
print(max_kupc(3, 2, ["KU", "KYOUDAI", "KYOTOUNIV"]))