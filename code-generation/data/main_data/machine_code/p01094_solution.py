def election_winner():
    while True:
        n = int(input())
        if n == 0:
            break
        votes = input().split()
        vote_count = {}
        winner = ''
        for i in range(n):
            if votes[i] in vote_count:
                vote_count[votes[i]] += 1
            else:
                vote_count[votes[i]] = 1
            max_votes = max(vote_count.values())
            candidates = [candidate for candidate, votes in vote_count.items() if votes == max_votes]
            if len(candidates) == 1:
                winner = candidates[0]
                print(winner, i+1)
                break
        if not winner:
            print('TIE')

election_winner()