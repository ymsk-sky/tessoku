from bisect import bisect_left

n = int(input())
xyl = [list(map(int, input().split())) for _ in range(n)]
xyl.sort(key=lambda e: (e[0], -e[1]))
INF = float("inf")
dp_y = [INF]
for x, y in xyl:
    if dp_y[-1] < y:
        dp_y.append(y)
    else:
        i = bisect_left(dp_y, y)
        dp_y[i] = y
print(len(dp_y))


"""
1<=n<=10**5
1<=x,y<=5*10**5

x1 < x2 < ... < xn として考えると単純にyに対してLISをすればよい.
xi=xjの時のためにxは昇順, xが同じ場合はyは降順にしておく.

5
30 50
10 30
40 10
50 20
40 60
3
"""