s = input()
t = input()
n = len(s)
m = len(t)
INF = float("inf")
dp = [[INF] * (m + 1) for _ in range(n + 1)]
dp[0] = [j for j in range(m + 1)]
for i in range(1, n + 1):
    dp[i][0] = i
for i, a in enumerate(s, start=1):
    for j, b in enumerate(t, start=1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + int(a != b))
ans = dp[n][m]
print(ans)
