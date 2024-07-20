def parallel_orthogonal(q, queries):
    for i in range(q):
        p0, p1, p2, p3 = queries[i]
        if (p1[1]-p0[1])*(p3[1]-p2[1]) + (p1[0]-p0[0])*(p3[0]-p2[0]) == 0:
            print("1")
        elif (p1[1]-p0[1])/(p1[0]-p0[0]) == (p3[1]-p2[1])/(p3[0]-p2[0]):
            print("2")
        else:
            print("0")

# Sample input
q = 3
queries = [((0,0), (3,0), (0,2), (3,2)), ((0,0), (3,0), (1,1), (1,4)), ((0,0), (3,0), (1,1), (2,2))]
parallel_orthogonal(q, queries)