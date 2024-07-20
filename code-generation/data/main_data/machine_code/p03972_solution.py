def min_total_cost(W, H, p, q):
    total_cost = 0
    for i in range(W):
        total_cost += p[i]
    for j in range(H):
        total_cost += q[j]
    return total_cost

#Sample Input 1
W1, H1 = 2, 2
p1 = [3, 5]
q1 = [2, 7]
print(min_total_cost(W1, H1, p1, q1))

#Sample Input 2
W2, H2 = 4, 3
p2 = [2, 4, 8, 1]
q2 = [2, 9, 3]
print(min_total_cost(W2, H2, p2, q2))