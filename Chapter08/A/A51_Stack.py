q = int(input())
stack = []
for _ in range(q):
    query = input()
    if query[0] == "1":
        stack.append(query[2:])
    elif query[0] == "2":
        print(stack[-1])
    else:
        stack.pop()
