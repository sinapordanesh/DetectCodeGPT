def judge_programs(s1, s2):
    if s1 == s2:
        return "IDENTICAL"
    else:
        s1_literals = [literal for i, literal in enumerate(s1.split('"')[1::2]) if i % 2 == 0]
        s2_literals = [literal for i, literal in enumerate(s2.split('"')[1::2]) if i % 2 == 0]
        
        if len(s1_literals) != len(s2_literals):
            return "DIFFERENT"
        
        diff_count = sum(1 for lit1, lit2 in zip(s1_literals, s2_literals) if lit1 != lit2)
        if diff_count == 1:
            return "CLOSE"
        else:
            return "DIFFERENT"