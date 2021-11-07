import sys

sys.stdin = open("input.txt", "r")


def isprime(num):
    sqr = int(num ** (1 / 2))

    if num == 1:
        return False

    for j in range(2, sqr + 1):
        if num % j == 0:
            return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(n // 2, 1, -1):
        if isprime(i) and isprime(n - i):
            print(i, n - i)
            break
