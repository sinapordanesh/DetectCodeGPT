from sys import stdin
input = stdin.readline
from time import time
from random import randint
from copy import deepcopy

start_time = time()

def calcScore(t, s, c):
    scores = [0]*26
    lasts = [0]*26
    for i in range(1, len(t)):
        scores[t[i]] += s[i][t[i]]
        dif = i - lasts[t[i]]
        scores[t[i]] -= c[t[i]] * dif * (dif-1) // 2
        lasts[t[i]] = i
    for i in range(26):
        dif = len(t) - lasts[i]
        scores[i] -= c[i] * dif * (dif-1) // 2
    return scores

def greedy(c, s):
    day_lim = len(s)
    socres = [0]*26
    t = [0]*day_lim
    lasts = [0]*26
    for i in range(1, day_lim):
        pls = [v for v in socres]
        mns = [v for v in socres]
        for j in range(26):
            pls[j] += s[i][j]
            mns[j] -= c[j] * (i - lasts[j])
        sum_mns = sum(mns)
        pt = sum_mns - mns[0] + pls[0]
        idx = 0
        for j in range(1, 26):
            tmp = sum_mns - mns[j] + pls[j]
            if pt < tmp:
                pt = tmp
                idx = j
        t[i] = idx
        lasts[idx] = i
        for j in range(26):
            if j == idx:
                socres[j] = pls[j]
            else:
                socres[j] = mns[j]
    return socres, t

def subGreedy(c, s, t, day):
    day_lim = len(s)
    socres = [0]*26
    t = [0]*day_lim
    lasts = [0]*26
    for i in range(1, day_lim):
        if day <= i:
            pls = [v for v in socres]
            mns = [v for v in socres]
            for j in range(26):
                pls[j] += s[i][j]
                mns[j] -= c[j] * (i - lasts[j])
            sum_mns = sum(mns)
            pt = sum_mns - mns[0] + pls[0]
            idx = 0
            for j in range(1, 26):
                tmp = sum_mns - mns[j] + pls[j]
                if pt < tmp:
                    pt = tmp
                    idx = j
            t[i] = idx
            lasts[idx] = i
            for j in range(26):
                if j == idx:
                    socres[j] = pls[j]
                else:
                    socres[j] = mns[j]
        else:
            scores[t[i]] += s[i][t[i]]
            lasts[t[i]] = i
            for j in range(26):
                dif = i - lasts[j]
                scores[j] -= c[j] * dif
    return socres, t

D = int(input())
c = list(map(int, input().split()))
s = [[0]*26 for _ in range(D+1)]
for i in range(1, D+1):
    s[i] = list(map(int, input().split()))

scores, t = greedy(c, s)
sum_score = sum(scores)

tm = time() - start_time

while tm < 1.86:
    typ = randint(1, 100)
    if typ <= 40:
        for _ in range(500):
            tmp_t = deepcopy(t)
            tmp_t[randint(1, D)] = randint(0, 25)
            tmp_scores = calcScore(tmp_t, s, c)
            sum_tmp_score = sum(tmp_scores)
            if sum_score < sum_tmp_score or (tm < 1.0 and randint(1, 1000) <= 1):
                sum_score = sum_tmp_score
                t = deepcopy(tmp_t)
                scores = deepcopy(tmp_scores)
    elif typ <= 99:
        for _ in range(100):
            tmp_t = deepcopy(t)
            dist = randint(1, 15)
            p = randint(1, D-dist)
            q = p + dist
            tmp_t[p], tmp_t[q] = tmp_t[q], tmp_t[p]
            tmp_scores = calcScore(tmp_t, s, c)
            sum_tmp_score = sum(tmp_scores)
            if sum_score < sum_tmp_score or (tm < 1.0 and randint(1, 200) <= 1):
                sum_score = sum_tmp_score
                t = deepcopy(tmp_t)
                scores = deepcopy(tmp_scores)
    elif typ <= 100:
        tmp_t = deepcopy(t)
        day = randint(D//4*3, D)
        tmp_scores, tmp_t = subGreedy(c, s, tmp_t, day)
        sum_tmp_score = sum(tmp_scores)
        if sum_score < sum_tmp_score:
            sum_score = sum_tmp_score
            t = deepcopy(tmp_t)
            scores = deepcopy(tmp_scores)
    tm = time() - start_time

for v in t[1:]:
    print(v+1)
