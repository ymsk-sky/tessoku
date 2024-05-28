n = int(input())
left = 0
right = 10**10
while right - left > 0.0001:
    mid = (left + right) / 2
    if mid**3 + mid > n:
        right = mid
    else:
        left = mid
print(right)
