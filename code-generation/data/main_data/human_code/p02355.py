class SegmentTree():
    def __init__(self, arr, func=min, ie=2**63):
        self.h = (len(arr) - 1).bit_length()
        self.n = 2**self.h
        self.ie = ie
        self.func = func
        self.tree = [ie for _ in range(2 * self.n)]
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(1, self.n)[::-1]:
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def set(self, idx, x):
        idx += self.n
        self.tree[idx] = x
        while idx:
            idx >>= 1
            self.tree[idx] = self.func(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, lt, rt):
        lt += self.n
        rt += self.n
        vl = vr = self.ie
        while rt - lt > 0:
            if lt & 1:
                vl = self.func(vl, self.tree[lt])
                lt += 1
            if rt & 1:
                rt -= 1
                vr = self.func(self.tree[rt], vr)
            lt >>= 1
            rt >>= 1
        return self.func(vl, vr)

N, K = map(int, input().split())
A = list(map(int, input().split()))

res = N + 1
st = SegmentTree([0] * K)
rt = 0

for lt in range(N):
    while rt < N and st.tree[1] == 0:
        if A[rt] <= K:
            st.set(A[rt] - 1, st.query(A[rt] - 1, A[rt]) + 1)
        rt += 1
    if st.tree[1] != 0:
        res = min(res, rt - lt)
    if A[lt] <= K:
        st.set(A[lt] - 1, st.query(A[lt] - 1, A[lt]) - 1)

print(res if res <= N else 0)
