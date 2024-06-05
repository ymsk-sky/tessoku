n, k = map(int, input().split())
al = list(map(int, input().split()))
dp = [0] * (n + 1)
for i in range(n + 1):
    win = False
    for a in al:
        if i >= a and dp[i - a] == 0:
            win = True
    if win:
        dp[i] = 1
    else:
        dp[i] = 0
print("First" if dp[n] else "Second")
