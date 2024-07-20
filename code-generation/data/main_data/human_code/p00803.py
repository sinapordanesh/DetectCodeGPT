"""
Problem A: Starship Hakodate-maru
https://onlinejudge.u-aizu.ac.jp/problems/1224
cannot be greater than 151200

Sample Input
100
64
50
20
151200
0
Output for the Sample Input
99
64
47
20
151200

maximum: 151200 = 39 × 39 × 39 + 81 × 82 × 83/6
n = 54  n^3 = 157464

n = 96 tetrahedral = 152096

"""

#cube and tetrahedral
cube = []
tetrahedral = []

def solve(n):
    min = 0
    diff_min = pow(10, 6)
    for i in cube:
        for j in tetrahedral:
            sum_value = i+j
            now_diff = n - sum_value
            if now_diff < diff_min and now_diff >= 0:
                diff_min = now_diff
                min = sum_value
                #print(n,i,j,sum_value,diff_min)

    return min

if __name__ == '__main__':

    for i in range(0, 55):
        cube.append(i**3)
    for i in range(0, 97):
        tetrahedral.append(i*(i+1)*(i+2)//6)

    ans = []
    while(True):
        n = int(input())
        if n == 0:
            break
        ans.append(solve(n))
    print(*ans, sep='\n')

