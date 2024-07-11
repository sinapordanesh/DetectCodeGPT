def Recording():
    n, c = map(int, input().split())
    num = 2*10**5+1 

    # チャンネルごとにimos配列
    imos = [[0]*num for _ in range(c)]
    
    # imos
    for _ in range(n):
        s, t, c0 = map(int, input().split())
        if imos[c0-1][s*2] < 0 and imos[c0-1][t*2-1] > 0:
            imos[c0-1][s*2] = 0
            imos[c0-1][t*2-1] = 0
        elif imos[c0-1][s*2] < 0:            
            imos[c0-1][s*2] = 0
            imos[c0-1][t*2] -= 1
        elif imos[c0-1][t*2-1] > 0:    
            imos[c0-1][s*2-1] += 1
            imos[c0-1][t*2-1] = 0
        else:
            imos[c0-1][s*2-1] += 1
            imos[c0-1][t*2] -= 1
    ans = [0 for _ in range(num)]
    for i in range(c):
        for j in range(1, num):
            imos[i][j] += imos[i][j-1]
            ans[j] += imos[i][j]
    print(max(ans))
    
if __name__ == '__main__':
    Recording()
    
