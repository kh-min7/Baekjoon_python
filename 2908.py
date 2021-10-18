import sys

sys.stdin = open("input.txt", "r")

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x //= 10
    return res

a, b = map(int, input().split())

if reverse(a) > reverse(b):
    print(reverse(a))
elif reverse(a) < reverse(b):
    print(reverse(b))
