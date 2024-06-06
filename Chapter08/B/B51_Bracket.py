s = input()
res = []
stack = []
for i, c in enumerate(s, start=1):
    if c == "(":
        stack.append(i)
    else:
        res.append((stack.pop(), i))
for re in res:
    print(*re)
