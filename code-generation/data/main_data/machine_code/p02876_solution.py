def max_probability_of_snuke_winning(N, beams):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    res = [0, 1]
    for a, b in beams:
        res[0] = max(res[0], res[1] * a // gcd(res[1], a))
        res[1] = res[1] * a // gcd(res[1], a)
        res[1] = res[1] * b // gcd(res[1], b)

    for i in range(N - 1):
        res[0] *= 2

    g = gcd(res[0], res[1])
    print(res[0] // g, res[1] // g)

# Sample Input 1
max_probability_of_snuke_winning(2, [[3, 2], [1, 2]])

# Sample Input 2
max_probability_of_snuke_winning(4, [[1, 5], [4, 7], [2, 1], [8, 4]])

# Sample Input 3
max_probability_of_snuke_winning(3, [[4, 1], [5, 2], [6, 3]])

# Sample Input 4
max_probability_of_snuke_winning(10, [[866111664, 178537096], [705445072, 318106937], [472381277, 579910117], [353498483, 865935868], [383133839, 231371336], [378371075, 681212831], [304570952, 16537461], [955719384, 267238505], [844917655, 218662351], [550309930, 62731178]])