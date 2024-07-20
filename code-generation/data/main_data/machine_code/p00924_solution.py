def min_swaps(N, M, bit_string, run_length_code):
    def count_swaps(bit_string, run_length_code):
        target = []
        for i, length in enumerate(run_length_code):
            target += [i % 2] * length
        swaps = 0
        for i in range(len(bit_string)):
            if bit_string[i] != target[i]:
                j = i + 1
                while bit_string[j] != target[i]:
                    j += 1
                bit_string[i:j+1] = bit_string[i:j+1][::-1]
                swaps += (j - i) // 2 + 1
        return swaps
    
    return count_swaps(bit_string, run_length_code)