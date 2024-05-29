from bisect import bisect_left

n, k = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))
dl = list(map(int, input().split()))
pl = []
for a in al:
    for b in bl:
        pl.append(a + b)
ql = []
for c in cl:
    for d in dl:
        ql.append(c + d)
ql.sort()
for p in pl:
    i = min(n**2 - 1, bisect_left(ql, k - p))
    if p + ql[i] == k:
        print("Yes")
        exit()
print("No")
