n, k = map(int, input().split())

M = 30
# dp[x][i]: 値iを2**x回操作したときの値
dp = [[0] * (n + 1) for _ in range(M + 1)]
for i in range(n + 1):
    j = sum([int(v) for v in str(i)])
    dp[0][i] = i - j
for x in range(1, M + 1):
    for i in range(n + 1):
        dp[x][i] = dp[x - 1][dp[x - 1][i]]

for i in range(1, n + 1):
    ans = i
    for x in range(M, -1, -1):
        if (k // (1 << x)) % 2 != 0:
            ans = dp[x][ans]
    print(ans)

"""
1<=n<=3*10**5
1<=k<=10**9
"""
