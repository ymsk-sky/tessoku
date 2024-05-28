h, w, n = map(int, input().split())
m = [[0] * (w + 1) for _ in range(h + 1)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    m[a - 1][b - 1] += 1
    m[c][d] += 1
    m[a - 1][d] -= 1
    m[c][b - 1] -= 1
for i in range(h):
    for j in range(w):
        m[i][j + 1] += m[i][j]
for j in range(w):
    for i in range(h):
        m[i + 1][j] += m[i][j]

for r in m[:-1]:
    print(*r[:-1])
