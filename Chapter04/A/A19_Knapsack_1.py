n, W = map(int, input().split())
wvl = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    w, v = wvl[i - 1]
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]
        if j - w >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

ans = max(dp[n])
print(ans)
