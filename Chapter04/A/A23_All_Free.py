n, m = map(int, input().split())
Tl = []
for _ in range(m):
    T = 0
    al = list(map(int, input().split()))
    for i, a in enumerate(al):
        if a == 1:
            T += 1 << i
    Tl.append(T)
INF = float("inf")
# dp[i][S]: (i+1)枚目までを使った集合Sの最小枚数
dp = [[INF] * (1 << n) for _ in range(m + 1)]
dp[0][0] = 0
for S in range(1 << n):
    for i, T in enumerate(Tl, start=1):
        dp[i][S] = min(dp[i][S], dp[i - 1][S])
        dp[i][S | T] = min(dp[i][S | T], dp[i - 1][S] + 1)
ans = dp[m][(1 << n) - 1]
print(-1 if ans == INF else ans)
