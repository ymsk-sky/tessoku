n = int(input())
hl = list(map(int, input().split()))
INF = float("inf")
dp = [INF] * n
dp[0] = 0
dp[1] = abs(hl[0] - hl[1])
for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(hl[i] - hl[i - 1]), dp[i - 2] + abs(hl[i] - hl[i - 2]))

i = n - 1
ans = []
while 1:
    ans.append(i + 1)
    if i == 0:
        break
    if dp[i - 1] + abs(hl[i] - hl[i - 1]) == dp[i]:
        i -= 1
    else:
        i -= 2
print(len(ans))
print(*ans[::-1])
