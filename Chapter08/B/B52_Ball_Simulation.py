from collections import deque

n, x = map(int, input().split())
a = list(input())
que = deque([x])
a[x - 1] = "@"
while que:
    pos = que.popleft()
    if pos - 2 >= 0 and a[pos - 2] == ".":
        a[pos - 2] = "@"
        que.append(pos - 1)
    if pos < n and a[pos] == ".":
        a[pos] = "@"
        que.append(pos + 1)
print(*a, sep="")
