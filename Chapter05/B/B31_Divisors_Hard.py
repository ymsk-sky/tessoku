n = int(input())
a = n // 3 + n // 5 + n // 7
b = n // (3 * 5) + n // (5 * 7) + n // (7 * 3)
c = n // (3 * 5 * 7)
ans = a - b + c
print(ans)
