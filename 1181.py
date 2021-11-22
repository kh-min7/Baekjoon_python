import sys

sys.stdin = open("input.txt", "r")

N = int(input())
arr = []

for _ in range(N):
    arr.append(input())

arr = set(arr)
arr = list(arr)

arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)