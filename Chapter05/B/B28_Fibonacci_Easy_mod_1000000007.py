n = int(input())
mod = 10**9 + 7
l = [0] * (n + 1)
l[1] = l[2] = 1
for i in range(3, n + 1):
    l[i] = l[i - 1] + l[i - 2]
    l[i] %= mod
print(l[n])
