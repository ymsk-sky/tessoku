M = 1500

n = int(input())
f = [[0] * (M + 1) for _ in range(M + 1)]
for _ in range(n):
    x, y = map(int, input().split())
    f[x][y] += 1
for i in range(1, M + 1):
    for j in range(1, M + 1):
        f[i][j] += f[i][j - 1]
for j in range(1, M + 1):
    for i in range(1, M + 1):
        f[i][j] += f[i - 1][j]

q = int(input())
l = [list(map(int, input().split())) for _ in range(q)]
for a, b, c, d in l:
    ans = f[c][d] + f[a - 1][b - 1] - f[c][b - 1] - f[a - 1][d]
    print(ans)
