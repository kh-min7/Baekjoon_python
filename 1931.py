import sys

sys.stdin = open("input.txt", "r")

n = int(input())
a = []

for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key=lambda x: (x[1], x[0]))

cnt = 0
ps = 0
for x, y in a:
    if x >= ps:
        cnt += 1
        ps = y

print(cnt)