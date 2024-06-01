n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
INF = float("inf")
dp = [-INF] * n
dp[0] = 0
for i, (a, b) in enumerate(zip(al, bl)):
    dp[a - 1] = max(dp[a - 1], dp[i] + 100)
    dp[b - 1] = max(dp[b - 1], dp[i] + 150)
ans = dp[n - 1]
print(ans)
