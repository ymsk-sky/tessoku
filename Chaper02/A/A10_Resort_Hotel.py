n = int(input())
al = list(map(int, input().split()))
p = [0] * (n + 1)
q = [0] * (n + 1)
for i in range(n):
    p[i + 1] = max(p[i], al[i])
    q[n - i - 1] = max(q[n - i], al[n - i - 1])
d = int(input())
lrl = [list(map(int, input().split())) for _ in range(d)]
for l, r in lrl:
    ans = max(p[l - 1], q[r])
    print(ans)
