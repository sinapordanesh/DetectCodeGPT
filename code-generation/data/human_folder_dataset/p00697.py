p_ch = [True] * 9
rot = ((0, 1, 2, 3), (1, 2, 3, 0), (2, 3, 0, 1), (3, 0, 1, 2))
adj = ['c'] * 13

# record indices of right and botoom adjacent edge label. 12 is invalid.
rec_adj = [[0, 2], [1, 3], [12, 4], [5, 7], [6, 8], [12, 9], [10, 12],
           [11, 12], [12, 12]]

# refernce indices to top and left adjacent edge label. 12 is invalid.
ref_adj = [[12, 12], [12, 0], [12, 1], [2, 12], [3, 5], [4, 6], [7, 12],
           [8, 10], [9, 11]]

tr = dict(zip("RGBWrgbw", "rgbwRGBW"))

def dfs(i = 0, a = []):
    if i == 9:
        global ans
        ans += 1
    else:
        for j, p in enumerate(pieces):
            if p_ch[j]:
                ati, ali = ref_adj[i]
                for t, r, b, l in rot:
                    if ati == 12 or tr[p[t]] == adj[ati]:
                        if ali == 12 or tr[p[l]] == adj[ali]:
                            ari, abi = rec_adj[i]
                            adj[ari] = p[r]
                            adj[abi] = p[b]
                            p_ch[j] = False
                            dfs(i + 1)
                            p_ch[j] = True

from sys import stdin
file_input = stdin

N = int(file_input.readline())

for line in file_input:
    pieces = line.split()
    ans = 0
    dfs()
    print(ans)
