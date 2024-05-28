n = int(input())
al = [0] + list(map(int, input().split()))
q = int(input())
lrl = [list(map(int, input().split())) for _ in range(q)]

for i in range(n):
    al[i + 1] += al[i]
for l, r in lrl:
    o = al[r] - al[l - 1]
    x = r - l + 1 - o
    ans = "draw"
    if o > x:
        ans = "win"
    elif o < x:
        ans = "lose"
    print(ans)
