a, b = map(int, input().split())
for v in range(a, b + 1):
    if 100 % v == 0:
        print("Yes")
        exit()
print("No")
