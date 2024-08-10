def shortest_possible_total_length_of_roads(N, table):
    total_length = sum(table[0])
    for i in range(N):
        for j in range(i+1, N):
            if table[i][j] != table[j][i]:
                return -1
            for k in range(N):
                if k != i and k != j and table[i][j] == table[i][k] + table[k][j]:
                    break
            else:
                if table[i][j] < table[i][k] + table[k][j]:
                    return -1
            total_length -= table[i][j]
    return total_length