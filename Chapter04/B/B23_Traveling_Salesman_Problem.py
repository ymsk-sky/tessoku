n = int(input())
xyl = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n)]
for i, (x1, y1) in enumerate(xyl):
    for j, (x2, y2) in enumerate(xyl):
        dist[i][j] = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
INF = float("inf")
# dp[S][v]: 集合Sに訪問済みで最後がvのときの最短時間
dp = [[INF] * n for _ in range(1 << n)]
dp[0][0] = 0
for S in range(1 << n):
    for v in range(n):
        for u in range(n):
            if (S >> u) & 1 == 0 and S > 0:
                continue
            if (S >> v) & 1:
                continue
            if dp[S | (1 << v)][v] > dp[S][u] + dist[u][v]:
                dp[S | (1 << v)][v] = dp[S][u] + dist[u][v]
ans = dp[(1 << n) - 1][0]
print(ans)
