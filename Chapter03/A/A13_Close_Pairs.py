n, k = map(int, input().split())
al = list(map(int, input().split()))
ans = 0
r = 0
for i, a in enumerate(al):
    while r < n:
        if a + k < al[r]:
            break
        r += 1
    r -= 1
    ans += r - i
print(ans)
