n, W = map(int, input().split())
wvl = [list(map(int, input().split())) for _ in range(n)]
INF = float("inf")
# dp[i][j]: i番目までで価値がjとなるときの最低重量
dp = [[INF] * (n*1000 + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    w, v = wvl[i - 1]
    for j in range(n*1000 + 1):
        dp[i][j] = dp[i - 1][j]
        if j - v >= 0:
            dp[i][j] = min(dp[i][j], dp[i - 1][j - v] + w)
ans = 0
for j in range(n*1000 + 1):
    if dp[n][j] <= W:
        ans = j
print(ans)
