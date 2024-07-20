def maximize_score(s):
    rock_count = 0
    paper_count = 0
    score = 0
    
    for gesture in s:
        if gesture == 'g':
            rock_count += 1
        else:
            paper_count += 1
        
        if paper_count <= rock_count:
            score += 1
    
    return score

# Test the function with the provided sample inputs
print(maximize_score("gpg"))
print(maximize_score("ggppgggpgg"))