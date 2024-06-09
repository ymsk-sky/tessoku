n, m = map(int, input().split())
edges = [[0, -i] for i in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1][0] += 1
    edges[b - 1][0] += 1
ans = -max(edges)[1] + 1
print(ans)
