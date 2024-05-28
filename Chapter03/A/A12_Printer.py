n, k = map(int, input().split())
al = list(map(int, input().split()))
left = 0
right = 10**9 + 1
while right - left > 1:
    mid = (left + right) // 2
    s = sum([mid // a for a in al])
    if s < k:
        left = mid
    else:
        right = mid
print(right)
