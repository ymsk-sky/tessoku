n = int(input())
al = list(map(int, input().split()))

d = {a: i for i, a in enumerate(sorted(set(al)), start=1)}
print(*[d[a] for a in al])
