def no_alternative_bridges(N, M, bridges):
    bridge_dict = {}
    for i in range(M):
        S, D, C = bridges[i]
        if (S, D) in bridge_dict:
            bridge_dict[(S, D)].append(C)
        else:
            bridge_dict[(S, D)] = [C]
    
    common_bridges = set(bridge_dict[(bridges[0][0], bridges[0][1])])
    for bridge in bridge_dict.values():
        common_bridges = common_bridges.intersection(set(bridge))
    
    return len(common_bridges), sum(common_bridges)

# Sample Input
N = 4
M = 4
bridges = [(1, 2, 3), (1, 3, 3), (2, 3, 3), (2, 4, 3)]

print(no_alternative_bridges(N, M, bridges))