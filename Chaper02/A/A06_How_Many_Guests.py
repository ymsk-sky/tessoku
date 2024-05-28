n, q = map(int, input().split())
al = [0] + list(map(int, input().split()))
lrl = [list(map(int, input().split())) for _ in range(q)]

for i in range(n):
    al[i + 1] += al[i]
for l, r in lrl:
    ans = al[r] - al[l - 1]
    print(ans)
