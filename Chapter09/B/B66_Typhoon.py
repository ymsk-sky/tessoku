class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

n, m = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
queries = []
default = [True] * m
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        default[x - 1] = False
    queries.append(query)
uf = UnionFind(n)
for i in range(m):
    if default[i]:
        a, b = abl[i]
        uf.unite(a - 1, b - 1)
ans = []
for query in queries[::-1]:
    if query[0] == 1:
        x = query[1]
        a, b = abl[x - 1]
        uf.unite(a - 1, b - 1)
    else:
        u, v = query[1:]
        res = "Yes" if uf.same(u - 1, v - 1) else "No"
        ans.append(res)
print(*ans[::-1], sep="\n")
