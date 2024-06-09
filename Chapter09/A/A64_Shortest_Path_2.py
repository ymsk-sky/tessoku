import heapq

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append((c, b))
    edges[b].append((c, a))
INF = float("inf")
dist = [INF] * n
dist[0] = 0
que = [(0, 0)]
heapq.heapify(que)
while que:
    cost, crt = heapq.heappop(que)
    if dist[crt] < cost:
        continue
    for nxt_cost, nxt in edges[crt]:
        if dist[nxt] <= cost + nxt_cost:
            continue
        dist[nxt] = cost + nxt_cost
        heapq.heappush(que, (cost + nxt_cost, nxt))
for d in dist:
    print(-1 if d == INF else d)
