mod = 10**9 + 7
l = [1]  # l[i]: i! % mod
for i in range(1, 10**5 + 1):
    l.append(l[-1] * i % mod)

def inv(n):
    """modを法とした逆元"""
    return pow(n, mod - 2, mod)

n, r = map(int, input().split())
ans = l[n] * inv(l[r]) * inv(l[n - r]) % mod
print(ans)
