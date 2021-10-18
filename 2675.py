import sys

sys.stdin = open("input.txt", "r")

t = int(input())

for _ in range(t):
    r, s = input().split()
    a = ""
    for i in s:
        a += int(r) * i

    print(a)