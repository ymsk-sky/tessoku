n, k = map(int, input().split())
al = list(map(int, input().split()))
ans = 0
right = 0
s = 0
for left, a in enumerate(al):
    while right < n and s + al[right] <= k:
        s += al[right]
        right += 1
    ans += right - left
    s -= a
print(ans)
