def count_anagram_pairs(N, strings):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(strings[i]) == sorted(strings[j]):
                count += 1
    return count

N = 3
strings = ['acornistnt', 'peanutbomb', 'constraint']
print(count_anagram_pairs(N, strings))

N = 2
strings = ['oneplustwo', 'ninemodsix']
print(count_anagram_pairs(N, strings))

N = 5
strings = ['abaaaaaaaa', 'oneplustwo', 'aaaaaaaaba', 'twoplusone', 'aaaabaaaaa']
print(count_anagram_pairs(N, strings))