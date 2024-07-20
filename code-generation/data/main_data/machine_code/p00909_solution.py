def weight_differences(N, M, data):
    weights = {}
    
    def get_weight(a, b):
        if a in weights and b in weights:
            return weights[b] - weights[a]
        else:
            return "UNKNOWN"
    
    for i in range(M):
        if data[i][0] == "!":
            a, b, w = data[i][1], data[i][2], data[i][3]
            weights[a] = weights.get(a, 0)
            weights[b] = weights.get(b, 0) + w
        elif data[i][0] == "?":
            a, b = data[i][1], data[i][2]
            print(get_weight(a, b))