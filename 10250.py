import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    room = []
    for i in range(1, w+1):
        for j in range(1, h+1):
            num = 100 * j + i
            room.append(num)

    print(room[n - 1])

