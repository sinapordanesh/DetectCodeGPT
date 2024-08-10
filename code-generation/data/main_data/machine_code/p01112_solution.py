def full_playoff_patterns(n, m, matches):
    if n == 0:
        return 0
    
    teams = set(range(1, n+1))
    played_matches = set()
    for match in matches:
        played_matches.add((match[0], match[1]))
    
    remaining_matches = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if (i, j) not in played_matches and (j, i) not in played_matches:
                remaining_matches.append((i, j))
    
    def dfs(remaining_matches, wins, losses):
        if len(remaining_matches) == 0:
            if len(set(wins.values())) == 1:
                return 1
            return 0
        
        match = remaining_matches[0]
        rest_matches = remaining_matches[1:]
        wins[match[0]] += 1
        losses[match[1]] += 1
        count = dfs(rest_matches, wins, losses)
        wins[match[0]] -= 1
        losses[match[1]] -= 1
        
        wins[match[1]] += 1
        losses[match[0]] += 1
        count += dfs(rest_matches, wins, losses)
        wins[match[1]] -= 1
        losses[match[0]] -= 1
        
        return count
    
    return dfs(remaining_matches, {i: 0 for i in teams}, {i: 0 for i in teams})

# Sample Input
print(full_playoff_patterns(5, 3, [(3, 2), (4, 1), (5, 1)]))
print(full_playoff_patterns(3, 1, [(1, 2)]))
print(full_playoff_patterns(5, 4, [(4, 1), (4, 2), (5, 1), (5, 2)]))