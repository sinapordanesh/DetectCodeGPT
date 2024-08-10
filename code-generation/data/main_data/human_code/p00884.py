def get_num(u, map, vis):
    if u in vis:
        return 0;
    else:
        vis[u] = True;
    ans = 0;
    if u in map:
        for v in map[u]:
            ans += get_num(v, map, vis);
    else:
            ans += 1;
    return ans;
def main():
    while True:
        n = int(input());
        if n == 0:
            break;
        edge = {}; name = {}; vis = {};
        for i in range(0, n):
            str = input();
            u = name[i] = str.split(':')[0];
            group = str.split(':')[1].split('.')[0].split(',');
            for v in group:
                if u in edge:
                    edge[u][v] = True;
                else:
                    edge[u] = {v:True};
        print(get_num(name[0], edge, vis));
main();