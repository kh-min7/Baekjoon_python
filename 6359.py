import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t):
    n = int(input())
    door = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            door[j] += 1

    ans = 0

    for i in range(1, n + 1):
        if door[i] % 2 == 1:
            ans += 1

    print(ans)
