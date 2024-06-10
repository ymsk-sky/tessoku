n = int(input())
al = [0] + list(map(int, input().split()))

dp = [0] * n
for i in range(n - 1, 0, -1):
    dp[al[i] - 1] += dp[i] + 1

print(*dp)
