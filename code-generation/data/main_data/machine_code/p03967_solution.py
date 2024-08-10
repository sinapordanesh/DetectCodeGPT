def maximize_score(s):
    rock_count = s.count('g')
    paper_count = s.count('p')
    
    return min(rock_count, paper_count)

#Input
s = "ggppgggpgg"

#Output
print(maximize_score(s))