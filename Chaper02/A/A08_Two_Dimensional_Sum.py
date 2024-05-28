h, w = map(int, input().split())
xl = [[0] * (w + 1)] + [[0] + list(map(int, input().split())) for _ in range(h)]
q = int(input())
l = [list(map(int, input().split())) for _ in range(q)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        xl[i][j] += xl[i][j - 1]
for j in range(1, w + 1):
    for i in range(1, h + 1):
        xl[i][j] += xl[i - 1][j]

for a, b, c, d in l:
    ans = xl[c][d] + xl[a - 1][b - 1] - xl[c][b - 1] - xl[a - 1][d]
    print(ans)
