def warshall_floyd(distance_table, point_size):
    for k in range(point_size):
        for i in range(point_size):
            for j in range(point_size):
                if distance_table[i][j] > distance_table[i][k] + distance_table[k][j]:
                    distance_table[i][j] = distance_table[i][k] + distance_table[k][j]

class bit:
    def __createtable():
        table = [None] * 64
        mask64 = (1 << 64) - 1
        hash = 0x03F566ED27179461
        for i in range(64):
            table[hash >> 58] = i
            hash = (hash << 1) & mask64
        return table
    
    __table = __createtable()

    def number_of_trailing_zeros(x):
        if x == 0:return 64
        mask64 = (1 << 64) - 1
        return bit.__table[((bit.lowest_one(x) * 0x03F566ED27179461) & mask64) >> 58]

    def lowest_one(i):
        return i & -i

def ccp(distance_table, point_size, v):
    if v:
        i = bit.number_of_trailing_zeros(v)
        v ^= (1 << i)
        return min(ccp(distance_table, point_size, v ^ (1 << j)) + distance_table[i][j] for j in range(point_size) if v & 1 << j)
    else:
        return 0


import sys
readline = sys.stdin.readline

point_size, e = map(int, readline().split())
distance_table = [[float('inf')] * point_size for _ in range(point_size)]
cost = 0
v = 0
for _ in range(e):
    s, t, d = map(int, readline().split())
    distance_table[s][t] = min(distance_table[s][t], d)
    distance_table[t][s] = min(distance_table[t][s], d)
    v ^= 1 << s ^ 1 << t
    cost += d

warshall_floyd(distance_table, point_size)
print(cost + ccp(distance_table, point_size, v))