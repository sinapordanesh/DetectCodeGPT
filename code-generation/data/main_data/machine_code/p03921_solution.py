def can_communicate(N, M, participants):
    languages = [set(participant[1:]) for participant in participants]
    
    for i in range(N):
        for j in range(i+1, N):
            if len(languages[i].intersection(languages[j])) == 0:
                return "NO"
    
    return "YES"