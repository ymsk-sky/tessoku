n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b)
    edges[b - 1].append(a)
for i in range(n):
    l = ", ".join([str(u) for u in sorted(edges[i])])
    print(f"{i + 1}: {{{l}}} ")
