n, x = map(int, input().split())
al = list(map(int, input().split()))
for a in al:
    if x == a:
        print("Yes")
        exit()
print("No")
