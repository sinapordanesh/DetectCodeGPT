from collections import Counter


def inverse_lookup(d: dict, x):
    for k, v in d.items():

        if v == x:
            return k

    # if x is not found
    return None


def num_of_nth_often(lst, nth):
    counter = Counter(lst)
    counted_list = sorted(list(counter.values()), reverse=True)

    if len(counted_list) < nth:
        return 0, None

    else:
        return counted_list[nth - 1], inverse_lookup(counter, counted_list[nth - 1])

n = int(input())
v = list(map(int, input().split()))

v_even = []
v_odd = []

for i in range(n):
    if i % 2 == 0:
        v_even.append(v[i])
    else:
        v_odd.append(v[i])

e1 = num_of_nth_often(v_even, 1)
e2 = num_of_nth_often(v_even, 2)
o1 = num_of_nth_often(v_odd, 1)
o2 = num_of_nth_often(v_odd, 2)

if e1[1] != o1[1]:
    rewrite_num = len(v_even) - e1[0] + len(v_odd) - o1[0]
    print(rewrite_num)
else:
    rewrite_num1 = len(v_even) - e1[0] + len(v_odd) - o2[0]
    rewrite_num2 = len(v_even) - e2[0] + len(v_odd) - o1[0]
    print(min(rewrite_num1, rewrite_num2))
