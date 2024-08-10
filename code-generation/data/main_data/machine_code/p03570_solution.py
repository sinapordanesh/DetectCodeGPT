def min_partitions(s):
    from collections import Counter
    cnt = Counter(s)
    odd_count = sum(1 for c in cnt.values() if c % 2 != 0)
    return max(1, odd_count)

# Test the function with sample inputs
print(min_partitions("aabxyyzz"))
print(min_partitions("byebye"))
print(min_partitions("abcdefghijklmnopqrstuvwxyz"))
print(min_partitions("abcabcxabcx"))