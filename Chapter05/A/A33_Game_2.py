n = int(input())
al = list(map(int, input().split()))
res = al[0]
for a in al[1:]:
    res ^= a
print("First" if res else "Second")
