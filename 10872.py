import sys

sys.stdin = open("input.txt", "r")


def factorial(x):
    if x == 0:
        return 1

    return x * (factorial(x - 1))


n = int(input())

print(factorial(n))
