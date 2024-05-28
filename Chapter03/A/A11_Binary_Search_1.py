from bisect import bisect_left

n, x = map(int, input().split())
al = list(map(int, input().split()))
i = bisect_left(al, x)
print(i + 1)
