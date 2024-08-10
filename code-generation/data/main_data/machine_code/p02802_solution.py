def contest_results(N, M, submissions):
    correct_answers = 0
    penalties = 0
    problems = {}
    
    for i in range(M):
        p, S = submissions[i]
        if S == 'AC' and p not in problems:
            correct_answers += 1
            problems[p] = 1
            penalties += problems.get(p, 0)
        elif S == 'WA':
            problems[p] = problems.get(p, 0) + 1
    
    return correct_answers, penalties

# Sample Input 1
print(contest_results(2, 5, [(1, 'WA'), (1, 'AC'), (2, 'WA'), (2, 'AC'), (2, 'WA')]))

# Sample Input 2
print(contest_results(100000, 3, [(7777, 'AC'), (7777, 'AC'), (7777, 'AC')]))

# Sample Input 3
print(contest_results(6, 0, []))