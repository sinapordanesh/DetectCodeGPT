def paper_cutting():
    n = int(input())
    strings = [input() for _ in range(n)]
    
    def can_be_created(s, target):
        freq_s = {}
        freq_target = {}
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1
        for char in target:
            freq_target[char] = freq_target.get(char, 0) + 1
        for char, count in freq_target.items():
            if char not in freq_s or freq_s[char] < count:
                return False
        return True
    
    target = strings[0]
    for s in strings[1:]:
        new_target = []
        for char in s:
            if char in target:
                new_target.append(char)
                target = target.replace(char, '', 1)
        target = ''.join(new_target)
    
    if not target:
        print()
    else:
        possible_strings = [target]
        for s in strings:
            if can_be_created(s, target):
                possible_strings.append(s)
        print(min(possible_strings))