n = int(input())
s = input()
t = s[::-1]
# dp[l][r]: l文字目からr文字目までの最長
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1
for l in range(1, n + 1):
    for r in range(1, n + 1):
        dp[l][r] = max(dp[l - 1][r], dp[l][r - 1])
        if s[l - 1] == t[r - 1]:
            dp[l][r] = max(dp[l][r], dp[l - 1][r - 1] + 1)
print(dp[n][n])

print(*dp, sep="\n")

"""
1<=n<=1000
"""
