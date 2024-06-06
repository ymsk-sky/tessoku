import heapq

q = int(input())
que = []
heapq.heapify(que)
for _ in range(q):
    query = input()
    com = int(query[0])
    if com == 1:
        heapq.heappush(que, int(query[2:]))
    elif com == 2:
        ans = heapq.heappop(que)
        print(ans)
        heapq.heappush(que, ans)
    else:
        heapq.heappop(que)
