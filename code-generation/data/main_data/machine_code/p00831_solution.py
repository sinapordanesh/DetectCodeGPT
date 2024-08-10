def confusing_login_names(n, d, names):
    def distance(s1, s2):
        if s1 == s2:
            return 0
        
        if len(s1) == 0:
            return len(s2)
        if len(s2) == 0:
            return len(s1)
        
        if s1[0] == s2[0]:
            return distance(s1[1:], s2[1:])
        
        delete_op = 1 + distance(s1[1:], s2)
        insert_op = 1 + distance(s1, s2[1:])
        replace_op = 1 + distance(s1[1:], s2[1:])
        swap_op = float('inf') if len(s1) < 2 or len(s2) < 2 else 1 + distance(s1[1], s2[0]) + distance(s1[0], s2[1])
        
        return min(delete_op, insert_op, replace_op, swap_op)
    
    def generate_confusing_pairs(names):
        pairs = []
        for i in range(len(names)):
            for j in range(i+1, len(names)):
                if distance(names[i], names[j]) <= d:
                    pairs.append((names[i], names[j]))
        return sorted(pairs)
    
    confusing_pairs = generate_confusing_pairs(names)
    for pair in confusing_pairs:
        print(f"{pair[0]},{pair[1]}")
    print(len(confusing_pairs))

# Sample Input
confusing_login_names(8, 2, ["omura", "toshio", "raku", "tanaka", "imura", "yoshoi", "hayashi", "miura"])
confusing_login_names(3, 1, ["tasaka", "nakata", "tanaka"])
confusing_login_names(1, 1, ["foo"])
confusing_login_names(5, 2, ["psqt", "abcdef", "abzdefa", "pqrst", "abdxcef"])