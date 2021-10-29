import sys

sys.stdin = open("input.txt", "r")

a = []
b = []
for _ in range(28):
    a.append(int(input()))

for i in range(1, 31):
    if i not in a:
        b.append(i)

b.sort()
for i in b:
    print(i)


