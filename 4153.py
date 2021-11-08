import sys

sys.stdin = open("input.txt", "r")

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break

    if a > c and a > b:
        tmp = c
        c = a
        a = tmp
    elif b > c and b > a:
        tmp = c
        c = b
        b = tmp

    if a * a + b * b == c * c:
        print("right")
    else:
        print("wrong")
