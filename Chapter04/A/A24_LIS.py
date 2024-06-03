from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))

INF = float("inf")
dp = [INF]
for a in al:
    if dp[-1] < a:
        dp.append(a)
    else:
        i = bisect_left(dp, a)
        dp[i] = a
print(len(dp))
