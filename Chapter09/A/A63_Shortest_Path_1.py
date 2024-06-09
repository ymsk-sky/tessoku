from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)
dist = [-1] * n
dist[0] = 0
que = deque([0])
while que:
    crt = que.popleft()
    for nxt in edges[crt]:
        if dist[nxt] != -1:
            continue
        dist[nxt] = dist[crt] + 1
        que.append(nxt)
for k in dist:
    print(k)
