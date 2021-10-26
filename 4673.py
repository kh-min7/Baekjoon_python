def SelfNum(n):
    n = n + sum(map(int, str(n)))
    return n

a = []
for i in range(1, 10000):
    a.append(SelfNum(i))

for i in range(1, 10000):
    if i not in a:
        print(i)