M = 3 * 10**5
l = [1] * (M + 1)
l[0] = l[1] = 0
for i in range(2, M + 1):
    if l[i] == 0:
        continue
    for j in range(i*2, M + 1, i):
        l[j] = 0

q = int(input())
xl = [int(input()) for _ in range(q)]
for x in xl:
    print("Yes" if l[x] else "No")
