from collections import defaultdict

n = int(input())
d = defaultdict(int)
ans = 0
for _ in range(n):
    a = int(input())
    ans += d[a]
    d[a] += 1
print(ans)
