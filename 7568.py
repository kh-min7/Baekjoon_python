import sys

sys.stdin = open("input.txt", "r")

n = int(input())

weight = []
height = []

for _ in range(n):
    x, y = map(int, input().split())
    weight.append(x)
    height.append(y)

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue

        if weight[i] < weight[j] and height[i] < height[j]:
            rank += 1

    print(rank)



