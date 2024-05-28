from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))
al.sort()
q = int(input())
xl = [int(input()) for _ in range(q)]
for x in xl:
    i = bisect_left(al, x)
    print(i)
