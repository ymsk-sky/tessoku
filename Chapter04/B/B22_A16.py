"""
A16 Dungeonを配るDPで実装
"""

n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
INF = float("inf")
dp = [INF] * n
dp[0] = 0
for i in range(n - 1):
    a = al[i]
    dp[i + 1] = min(dp[i + 1], dp[i] + a)
    if i == n - 2:
        continue
    b = bl[i]
    dp[i + 2] = min(dp[i + 2], dp[i] + b)
ans = dp[n - 1]
print(ans)
