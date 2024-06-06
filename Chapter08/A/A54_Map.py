q = int(input())
d = {}
for _ in range(q):
    query = input().split()
    com = int(query[0])
    if com == 1:
        name, score = query[1:]
        d[name] = score
    else:
        name = query[1]
        print(d[name])
