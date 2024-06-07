"""ハッシュ化
S[a-1:b]とS[c-1:d]が同じかを判定する
1 <= N <= 2*10**5
1 <= Q <= 2*10**5
衝突は1/modなので充分実用的
"""

mod = 2147483647

n, q = map(int, input().split())
s = input()

# bl[i]: B**i = 100**i
bl = [1]
for i in range(1, n + 1):
    bl.append(100 * bl[-1] % mod)

# hl[i]: Hi
hl = [0]
for c in s:
    o = ord(c) - 96
    hl.append((100 * hl[-1] + o) % mod)

def hash_value(l, r):
    """s[l-1:r]のハッシュ値を返す"""
    return (hl[r] - (hl[l - 1] * bl[r - l + 1])) % mod

abcdl = [list(map(int, input().split())) for _ in range(q)]
for a, b, c, d in abcdl:
    if hash_value(a, b) == hash_value(c, d):
        print("Yes")
    else:
        print("No")
