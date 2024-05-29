from bisect import bisect_left

n, k = map(int, input().split())
al = list(map(int, input().split()))

m = n // 2
n -= m
al, bl = al[:m], al[m:]

pl = []
for i in range(1 << m):
    p = 0
    for j in range(m):
        if (i >> j) & 1:
            p += al[j]
    pl.append(p)
ql = []
for i in range(1 << n):
    q = 0
    for j in range(n):
        if (i >> j) & 1:
            q += bl[j]
    ql.append(q)
ql.sort()
for p in pl:
    i = min(len(ql) - 1, bisect_left(ql, k - p))
    if p + ql[i] == k:
        print("Yes")
        exit()
print("No")
