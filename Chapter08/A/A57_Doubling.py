n, q = map(int, input().split())
al = list(map(int, input().split()))

M = 30  # Y<=10**9, 10**9<2**30のため30あたりまで計算すれば足りる

# dp[d][i]: 穴(i - 1)から2**d日後の場所
dp = [[0] * n for _ in range(M + 1)]
for i in range(n):
    dp[0][i] = al[i] - 1
for d in range(1, M + 1):
    for i in range(n):
        dp[d][i] = dp[d - 1][dp[d - 1][i]]

xyl = [list(map(int, input().split())) for _ in range(q)]
for x, y in xyl:
    crt = x - 1
    for d in range(M, -1, -1):
        if (y // (1 << d)) % 2 != 0:
            crt = dp[d][crt]
    print(crt + 1)
