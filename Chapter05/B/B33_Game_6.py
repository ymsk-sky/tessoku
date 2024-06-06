n, h, w = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(n)]
res = (abl[0][0] - 1) ^ (abl[0][1] - 1)
for a, b in abl[1:]:
    res ^= a - 1
    res ^= b - 1
print("First" if res else "Second")
