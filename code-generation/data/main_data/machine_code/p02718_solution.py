def popular_items(N, M, votes):
    total_votes = sum(votes)
    votes.sort(reverse=True)
    
    if votes[M-1] >= total_votes/(4*M):
        return "Yes"
    else:
        return "No"