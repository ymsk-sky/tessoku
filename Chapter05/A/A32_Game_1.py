n, a, b = map(int, input().split())
# dp[i]: 残りi個の時, 先手が勝てるか
dp = [0] * (n + 1)
for i in range(n + 1):
    if i >= a and dp[i - a] == 0:
        dp[i] = 1
    elif i >= b and dp[i - b] == 0:
        dp[i] = 1
    else:
        dp[i] = 0
if dp[n]:
    print("First")
else:
    print("Second")

"""
2<=n<=10**5
1<=a<b<=n
"""