import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)

ans = []
vis = [False] * n
def dfs(crt):
    vis[crt] = True
    ans.append(crt + 1)
    if crt == n - 1:
        print(*ans)
        exit()
    for nxt in edges[crt]:
        if vis[nxt]:
            continue
        dfs(nxt)
    ans.pop()

dfs(0)
