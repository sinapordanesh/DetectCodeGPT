def color_map():
    while True:
        n = int(input())
        if n == 0:
            break
        countries = {}
        adj_c = {}
        colors = {}
        for i in range(n):
            country = input()
            vertices = []
            while True:
                v = input()
                if v == "-1":
                    break
                vertices.append(tuple(map(int, v.split())))
            countries[country] = vertices
            colors[country] = -1
            adj_c[country] = set()
        
        for c1, v1 in countries.items():
            for c2, v2 in countries.items():
                if c1 != c2:
                    if any([any([((v1[i-1][0]-v1[i][0], v1[i-1][1]-v1[i][1]) == (v2[j-1][0]-v2[j][0], v2[j-1][1]-v2[j][1])) or ((v1[i-1][0]-v1[i][0], v1[i-1][1]-v1[i][1]) == (v2[j][0]-v2[j-1][0], v2[j][1]-v2[j-1][1])) for i in range(len(v1))]) for j in range(len(v2))]):
                        adj_c[c1].add(c2)
                        adj_c[c2].add(c1)
        
        def color(c):
            used = set()
            for a in adj_c[c]:
                if colors[a] != -1:
                    used.add(colors[a])
            for i in range(4):
                if i not in used:
                    return i
        
        for c in countries.keys():
            colors[c] = color(c)
        
        print(max(colors.values()) + 1)