def can_communicate(N, M, participants):
    languages = {}
    participants_list = []
    
    for i in range(N):
        participants_list.append(set(participants[i][1:]))
        for lang in participants[i][1:]:
            if lang not in languages:
                languages[lang] = set()
            languages[lang].add(i)
    
    for i in range(N):
        can_communicate = set()
        for lang in participants_list[i]:
            can_communicate = can_communicate.union(languages[lang])
        if len(can_communicate) != N:
            return "NO"
    
    return "YES"

# Sample Input
N = 4
M = 6
participants = [[3, 1, 2, 3], [2, 4, 2], [2, 4, 6], [1, 6]]
print(can_communicate(N, M, participants))

N = 4
M = 4
participants = [[2, 1, 2], [2, 1, 2], [1, 3], [2, 4, 3]]
print(can_communicate(N, M, participants))