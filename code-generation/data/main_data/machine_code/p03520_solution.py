def restore_edge_lengths(N, edges, distances):
    total_distance = sum(distances)
    edge_lengths = []
    for i in range(N-1):
        a = edges[i][0]
        b = edges[i][1]
        edge_length = (total_distance - distances[a-1] - distances[b-1]) / 2
        edge_lengths.append(int(edge_length))
    return edge_lengths