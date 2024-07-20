def prefix_suffix_search(N, Q, words, queries):
    result = []
    for prefix, suffix in queries:
        count = 0
        for word in words:
            if word.startswith(prefix) and word.endswith(suffix):
                count += 1
        result.append(count)
    return result

# Sample input
N = 6
Q = 7
words = ["appreciate", "appropriate", "acceptance", "ace", "acm", "acetylene"]
queries = [("appr", "iate"), ("a", "e"), ("a", "a"), ("ac", "ce"), ("ace", "e"), ("acceptance", "acceptance"), ("no", "match")]

print(*prefix_suffix_search(N, Q, words, queries), sep="\n")