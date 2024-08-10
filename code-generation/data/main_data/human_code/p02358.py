# -*- coding: utf-8 -*-
import io, sys
import bisect


def main():
    N = int( sys.stdin.readline() )
    x1y1x2y2_list = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
    
    X1 = [a for a,b,c,d in x1y1x2y2_list]
    X2 = [c for a,b,c,d in x1y1x2y2_list]
    Y1 = [b for a,b,c,d in x1y1x2y2_list]
    Y2 = [d for a,b,c,d in x1y1x2y2_list]

    all_X = compress(X1,X2)
    all_Y = compress(Y1,Y2)

    matrix =[ [0]*len(all_X) for _ in range(len(all_Y)) ]

    for i in range(N):
        matrix[ Y1[i] ][ X1[i] ] += 1
        matrix[ Y2[i] ][ X2[i] ] += 1
        matrix[ Y2[i] ][ X1[i] ] -= 1
        matrix[ Y1[i] ][ X2[i] ] -= 1

    for row in range(len(matrix)):
        for col in range(1, len(matrix[0])):
            matrix[row][col] += matrix[row][col-1]
    
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] += matrix[row-1][col]

    ans = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                area = (all_X[col+1] - all_X[col]) * (all_Y[row+1] - all_Y[row])
                ans += area

    print(ans)


def compress(A1 :list, A2 :list):
    all_A = []
    #delta = [-1, 0, 1]
    delta = [0]

    for a in (A1 + A2):
        for d in delta:
            all_A.append(a + d)
    
    all_A = sorted(set(all_A))

    for i in range(len(A1)):
        A1[i] = bisect.bisect_left(all_A, A1[i])
        A2[i] = bisect.bisect_left(all_A, A2[i])
    
    return all_A


if __name__ == "__main__":
    main()

