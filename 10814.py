import sys

sys.stdin = open("input.txt", "r")

N = int(input())
arr = []

for _ in range(N):
    age, name = input().split()
    age = int(age)
    arr.append((age, name))

arr.sort(key=lambda x: x[0])

for i in arr:
    print(i[0], i[1])