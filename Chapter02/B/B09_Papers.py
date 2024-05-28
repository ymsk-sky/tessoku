M = 1500

n = int(input())
f = [[0] * (M + 1) for _ in range(M + 1)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    f[a][b] += 1
    f[c][d] += 1
    f[a][d] -= 1
    f[c][b] -= 1
for i in range(M):
    for j in range(M):
        f[i][j + 1] += f[i][j]
for j in range(M):
    for i in range(M):
        f[i + 1][j] += f[i][j]
ans = 0
for i in range(M):
    for j in range(M):
        if f[i][j] > 0:
            ans += 1
print(ans)
