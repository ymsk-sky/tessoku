n, k = map(int, input().split())
ans = 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        c = k - (a + b)
        if 0 < c <= n:
            ans += 1
print(ans)
