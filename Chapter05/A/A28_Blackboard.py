n = int(input())
ans = 0
mod = 10_000
for _ in range(n):
    t, a = input().split()
    a = int(a)
    if t == "+":
        ans += a
    elif t == "-":
        ans -= a
    elif t == "*":
        ans *= a
    ans %= mod
    print(ans)
