from collections import deque

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [input() for _ in range(r)]

dist = [[-1] * c for _ in range(r)]
dist[sy - 1][sx - 1] = 0
que = deque([(sy - 1, sx - 1)])
while que:
    i, j = que.popleft()
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if 0 > u or u >= r or 0 > v or v >= c:
            continue
        if maze[u][v] == "#":
            continue
        if dist[u][v] != -1:
            continue
        dist[u][v] = dist[i][j] + 1
        que.append((u, v))
ans = dist[gy - 1][gx - 1]
print(ans)
