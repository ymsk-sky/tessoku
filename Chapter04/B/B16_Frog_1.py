n = int(input())
hl = list(map(int, input().split()))
INF = float("inf")
dp = [INF] * n
dp[0] = 0
dp[1] = abs(hl[0] - hl[1])
for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(hl[i] - hl[i - 1]), dp[i - 2] + abs(hl[i] - hl[i - 2]))
print(dp[n - 1])
