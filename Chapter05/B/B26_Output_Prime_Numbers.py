M = 10**6
l = [1] * (M + 1)
l[0] = l[1] = 0
for i in range(2, M + 1):
    if l[i] == 0:
        continue
    for j in range(i*2, M + 1, i):
        l[j] = 0

n = int(input())
for i in range(n + 1):
    if l[i]:
        print(i)
