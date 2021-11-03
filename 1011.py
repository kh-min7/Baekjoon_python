import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    distance = y - x

    n = 2

    if distance < 3:
        print(distance)

    else:
        while distance not in range(n * n - n + 1, n * n + n + 1):
            n += 1

        if distance <= n * n:
            print(2 * n - 1)
        else:
            print(2 * n)
