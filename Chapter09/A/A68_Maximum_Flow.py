"""最大フロー
Ford-Fulkerson法
"""

import sys
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    ia = len(edges[a])
    ib = len(edges[b])
    # 辺の行先,重み,逆辺インデックスを保持
    edges[a].append([b, c, ib])
    edges[b].append([a, 0, ia])

vis = [False] * n

def dfs(crt, goal, crt_flow):
    """DFS
    crt: 現在項
    goal: 最終目的頂
    crt_flow: スタートからcrtまでの残余グラフの辺の重みの最小値

    returns: 流したフローの量(流せない場合は0)
    """
    if crt == goal:
        return crt_flow
    vis[crt] = True
    for i, (nxt, nxt_flow, j) in enumerate(edges[crt]):
        if nxt_flow == 0:  # 容量0の辺は使用しない
            continue
        if vis[nxt]:  # 既に訪問済みの項は使用しない
            continue
        flow = dfs(nxt, goal, min(crt_flow, nxt_flow))  # 最終目的項を探索
        if flow > 0:
            # フロー分だけ残余グラフの重みを増減させる
            edges[crt][i][1] -= flow
            edges[nxt][j][1] += flow
            return flow
    return 0

ans = 0
while 1:
    vis = [False] * n
    f = dfs(0, n - 1, 10**10)
    if f == 0:
        break
    ans += f
print(ans)
