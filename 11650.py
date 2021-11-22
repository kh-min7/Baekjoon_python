import sys

sys.stdin = open("input.txt", "r")

N = int(input())
arr = []

for i in range(N):
    [a, b] = map(int, input().split())
    arr.append([a, b])

arr.sort()

for j in arr:
    print(j[0], j[1])
