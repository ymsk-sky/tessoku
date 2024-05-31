n = int(input())
pal = [list(map(int, input().split())) for _ in range(n)]
# dp[i][j]: (i,j)が残った状態の時の最大値
dp = [[0] * n for _ in range(n)]
dp[0][n - 1] = 0  # 0 ~ (n-1)のすべてが残っている状態
for m in range(n - 2, -1, -1):
    for l in range(n - m):
        r = l + m
        score1 = 0
        score2 = 0
        if l - 1 >= 0:
            p, a = pal[l - 1]
            if l <= p - 1 <= r:
                score1 = a
        if r + 1 <= n - 1:
            p, a = pal[r + 1]
            if l <= p - 1 <= r:
                score2 = a
        if l == 0:
            dp[l][r] = dp[l][r + 1] + score2
        elif r == n - 1:
            dp[l][r] = dp[l - 1][r] + score1
        else:
            dp[l][r] = max(dp[l][r + 1] + score2, dp[l - 1][r] + score1)
ans = max([dp[i][i] for i in range(n)])
print(ans)
