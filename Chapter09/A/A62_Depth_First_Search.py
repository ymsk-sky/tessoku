import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)

vis = [False] * n
def dfs(crt):
    vis[crt] = True
    for nxt in edges[crt]:
        if vis[nxt]:
            continue
        dfs(nxt)

dfs(0)
if all(vis):
    print("The graph is connected.")
else:
    print("The graph is not connected.")
