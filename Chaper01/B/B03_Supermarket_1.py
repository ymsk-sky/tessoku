n = int(input())
al = list(map(int, input().split()))
for i in range(n):
    a1 = al[i]
    for j in range(i + 1, n):
        a2 = al[j]
        for k in range(j + 1, n):
            a3 = al[k]
            if a1 + a2 + a3 == 1000:
                print("Yes")
                exit()
print("No")
