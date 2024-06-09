n = int(input())
al = list(map(int, input().split()))
ans = []
stack_lv2 = []
for i, a in enumerate(al, start=1):
    while stack_lv2:
        if stack_lv2[-1][1] < a:
            stack_lv2.pop()
        else:
            break
    if stack_lv2:
        ans.append(stack_lv2[-1][0])
    else:
        ans.append(-1)
    stack_lv2.append((i, a))
print(*ans)
