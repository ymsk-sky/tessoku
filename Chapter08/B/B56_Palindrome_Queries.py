n, q = map(int, input().split())
s = input()
lrl = [list(map(int, input().split())) for _ in range(q)]

t = s[::-1]

mod = 2147483647
# bl[i]: B**i = 100**i
bl = [1]
for i in range(1, n + 1):
    bl.append(100 * bl[-1] % mod)
# hl[i]: Hi, gl[i]: Gi
hl = [0]
gl = [0]
for c, d in zip(s, t):
    o = ord(c) - 96
    hl.append((100 * hl[-1] + o) % mod)
    o = ord(d) - 96
    gl.append((100 * gl[-1] + o) % mod)

def hash_value(l, r):
    """s[l-1:r]のハッシュ値を返す"""
    return (hl[r] - (hl[l - 1] * bl[r - l + 1])) % mod

def hash_value_rev(l, r):
    """t[l-1:r]のハッシュ値を返す"""
    return (gl[r] - (gl[l - 1] * bl[r - l + 1])) % mod

for l, r in lrl:
    if hash_value(l, r) == hash_value_rev(n - r + 1, n - l + 1):
        print("Yes")
    else:
        print("No")
