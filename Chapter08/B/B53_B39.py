import heapq

n, d = map(int, input().split())
que = []
heapq.heapify(que)
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(que, (-y, -x))
ans = 0
for e in range(1, d + 1):
    l = []
    while que:
        y, x = heapq.heappop(que)
        if e >= -x:
            ans -= y
            break
        else:
            l.append((y, x))
    for y, x in l:
        heapq.heappush(que, (y, x))
print(ans)
