def game_winner(N, edges):
    adj_list = {}
    for i in range(1, N+1):
        adj_list[i] = []
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    def dfs(node, parent, coins):
        coins += 1
        winner = True
        for neighbor in adj_list[node]:
            if neighbor != parent:
                winner &= dfs(neighbor, node, coins)
        
        if winner and coins % 2 == 1:
            return False
        return True
    
    if dfs(1, -1, 0):
        return "Second"
    else:
        return "First"