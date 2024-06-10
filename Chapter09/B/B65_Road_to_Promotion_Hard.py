import sys
sys.setrecursionlimit(10**7)

n, t = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)
dist = [-1] * n
def dfs(u, d):
    dist[u] = d
    for v in edges[u]:
        if dist[v] >= 0:
            continue
        dfs(v, d + 1)
dfs(t - 1, 0)
l = sorted(range(n), key=lambda i: dist[i], reverse=True)

dp = [0] * n
fin = [False] * n
for i in l:
    fin[i] = True
    for j in edges[i]:
        if fin[j]:
            continue
        dp[j] = max(dp[j], dp[i] + 1)
print(*dp)
