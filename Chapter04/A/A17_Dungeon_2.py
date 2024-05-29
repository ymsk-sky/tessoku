INF = float("inf")

n = int(input())
al = [INF] + list(map(int, input().split()))
bl = [INF] * 2 + list(map(int, input().split()))
dp = [INF] * (n + 1)
dp[1] = 0
for i in range(2, n + 1):
    dp[i] = min(dp[i - 1] + al[i - 1], dp[i - 2] + bl[i - 1])
i = n
ans = []
while 1:
    ans.append(i)
    if i == 1:
        break
    if dp[i - 1] + al[i - 1] == dp[i]:
        i -= 1
    else:
        i -= 2
print(len(ans))
print(*ans[::-1])
