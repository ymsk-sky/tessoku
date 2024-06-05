h, w = map(int, input().split())
mod = 10**9 + 7

l = [1]
for i in range(1, 2*10**5):
    l.append(l[-1] * i % mod)

def inv(n):
    """modを法とした逆元"""
    return pow(n, mod - 2, mod)

ans = l[h + w - 2] * inv(l[h - 1]) * inv(l[w - 1]) % mod
print(ans)
