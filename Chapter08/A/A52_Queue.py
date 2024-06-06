from collections import deque

q = int(input())
que = deque()
for _ in range(q):
    query = input()
    com = int(query[0])
    if com == 1:
        que.append(query[2:])
    elif com == 2:
        print(que[0])
    else:
        que.popleft()
