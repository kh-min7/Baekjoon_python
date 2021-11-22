import sys

sys.stdin = open("input.txt", "r")

N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda a:(a[1], a[0]))

for [i,j] in arr:
    print(i, j)
