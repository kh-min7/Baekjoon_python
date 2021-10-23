import sys

sys.stdin = open("input.txt", "r")

h, m = map(int, input().split())

a = list(range(24))
b = list(range(60))

if m < 45:
    h = a[h-1]
    m = b[m-45]
elif m >= 45:
    m = b[m-45]

print(h, m)