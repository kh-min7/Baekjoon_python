import sys

sys.stdin = open("input.txt", "r")

while True:
    a, b = map(int, input().split())
    if a > 0:
        print(a+b)
    else:
        break