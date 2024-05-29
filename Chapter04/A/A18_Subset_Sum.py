n, s = map(int, input().split())
al = list(map(int, input().split()))
dp = [[0] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    a = al[i - 1]
    for j in range(s + 1):
        dp[i][j] += dp[i - 1][j]
        if j - a < 0:
            continue
        dp[i][j] += dp[i - 1][j - a]
print("Yes" if dp[n][s] > 0 else "No")
