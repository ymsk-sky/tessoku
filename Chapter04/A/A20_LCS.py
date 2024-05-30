s = input()
t = input()
n = len(s)
m = len(t)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i, a in enumerate(s, start=1):
    for j, b in enumerate(t, start=1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if a == b:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
ans = dp[n][m]
print(ans)
