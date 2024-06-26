from bisect import bisect_left, bisect_right

def segfunc(x, y):
    return min(x, y)

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i + 1])

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k^1])
            k >>= 1

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k^1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


INF = float("inf")
n, l, r = map(int, input().split())
xl = list(map(int, input().split()))
dp = [INF] * n
dp[0] = 0
st = SegTree(
    init_val=dp, segfunc=segfunc, ide_ele=INF,
)
for i in range(1, n):
    x = xl[i]
    li = bisect_left(xl, x - r)
    ri = bisect_right(xl, x - l)
    cnt = st.query(li, ri) + 1
    st.update(i, cnt)
ans = st.query(n - 1, n)
print(ans)
