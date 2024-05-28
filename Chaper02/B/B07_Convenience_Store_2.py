t = int(input())
n = int(input())
acc = [0] * (t + 1)
for _ in range(n):
    l, r = map(int, input().split())
    acc[l] += 1
    acc[r] -= 1
for i in range(t):
    acc[i + 1] += acc[i]
print(*acc[:-1], sep="\n")
