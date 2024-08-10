def subsets(n, k, b):
    def decimal_to_binary(num, n):
        binary = bin(num)[2:]
        return '0' * (n - len(binary)) + binary

    def get_subsets(k, b):
        subsets = []
        for i in range(2 ** k):
            subset = []
            for j in range(k):
                if (i >> j) & 1:
                    subset.append(b[j])
            subsets.append(subset)
        return subsets

    subsets = get_subsets(k, b)
    subsets.sort(key=lambda x: sum(1 << i for i in x))

    for subset in subsets:
        decimal = sum(1 << i for i in subset)
        print(f"{decimal}:", " ".join(map(str, subset)))

# Sample Input
subsets(4, 2, [0, 2])